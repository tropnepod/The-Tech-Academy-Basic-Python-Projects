import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



conn = sqlite3.connect('test2.db')



with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_text_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT \
                )")
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_text_files(col_filename) VALUES (?)",\
                    [file])
        else:
            continue
    conn.commit()

    cur.execute("SELECT col_filename FROM tbl_text_files")
    varFiles = cur.fetchall()
    for row in varFiles:
        msg = "File Name: {}".format(row)
        print(msg)

conn.close()

