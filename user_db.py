import sqlite3

DATABASE_PATH = "user_bind_data.db"

def get_db_connection():
    """获取数据库连接"""
    return sqlite3.connect(DATABASE_PATH)

def query_maimai_uid(qq_number):
    """根据QQNumber查询绑定的maimaiUID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT maimaiUID FROM RemiBot_QQBind WHERE QQNumber = ?', (qq_number,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()

def bind_or_update_user(qq_number, maimai_uid):
    """绑定或更新QQNumber对应的maimaiUID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM RemiBot_QQBind WHERE QQNumber = ?', (qq_number,))
        row = cursor.fetchone()
        if row:
            cursor.execute('''
            UPDATE RemiBot_QQBind
            SET maimaiUID = ?
            WHERE QQNumber = ?
            ''', (maimai_uid, qq_number))
        else:
            cursor.execute('''
            INSERT INTO RemiBot_QQBind (QQNumber, maimaiUID)
            VALUES (?, ?)
            ''', (qq_number, maimai_uid))
        conn.commit()
        return True  # 操作成功
    except Exception as e:
        print(f"数据库操作出错: {e}")
        return False
    finally:
        conn.close()

def initialize_database():
    """初始化数据库表"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS RemiBot_QQBind (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            QQNumber TEXT NOT NULL UNIQUE,
            maimaiUID TEXT NOT NULL
        )
        ''')
        conn.commit()
    finally:
        conn.close()

def main():
    """命令行交互主程序"""
    initialize_database()  # 确保数据库表已初始化
    while True:
        print("\nRemiBot UserDB CLI")
        print("1. 绑定或更新QQNumber和maimaiUID")
        print("2. 查询maimaiUID")
        print("3. 退出")
        choice = input("请选择操作（1/2/3）: ")

        if choice == '1':
            qq_number = input("请输入QQNumber: ")
            maimai_uid = input("请输入maimaiUID: ")
            if bind_or_update_user(qq_number, maimai_uid):
                print(f"成功绑定或更新QQNumber {qq_number} 和 maimaiUID {maimai_uid}")
            else:
                print("绑定或更新失败，请检查输入。")
        elif choice == '2':
            qq_number = input("请输入要查询的QQNumber: ")
            maimai_uid = query_maimai_uid(qq_number)
            if maimai_uid:
                print(f"QQNumber为{qq_number}的maimaiUID是: {maimai_uid}")
            else:
                print(f"未找到QQNumber为{qq_number}的记录。")
        elif choice == '3':
            print("退出程序。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()
