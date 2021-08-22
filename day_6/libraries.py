# pip ----> Python Installation Package (.jar)
# https://pypi.org ----> community
# pip install <module>
# import urllib3
# API - GET, POST, DELETE, PUT
# http = urllib3.PoolManager()
# response = http.request(
#     "GET", "http://api.covid19india.org/v4/min/data.min.json")
# print(response.status)
# print(response)
# pip install "project"

import tkinter as tk  # UI for operating systems

root = tk.Tk()   # creating an UI or instance


def showEntryForm():
    print("Your Data: ", entry_1.get(),
          entry_2.get(), entry_3.get(), entry_4.get())
    # mobile = entry_4.get()
    # if mobile == "9047048344":
    #     print("It is praveen's number")
    # output: Your Data:  Praveen Kumar pravileaf@gmail.com 904704344


root.title("Basic Form")
tk.Label(root, text="First Name").grid(row=1)
tk.Label(root, text="Last Name").grid(row=2)
tk.Label(root, text="E-mail ID").grid(row=3)
tk.Label(root, text="Mobile Number").grid(row=4)

entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)
entry_3 = tk.Entry(root)
entry_4 = tk.Entry(root)


entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
entry_3.grid(row=3, column=1)
entry_4.grid(row=4, column=1)

tk.Button(root, text="Close", command=root.quit).grid(
    row=5, column=0, pady=6, sticky=tk.W)
tk.Button(root, text="Show", command=showEntryForm).grid(
    row=6, column=0, pady=6, sticky=tk.W)

root.mainloop()  # main object to create or develop an UI
