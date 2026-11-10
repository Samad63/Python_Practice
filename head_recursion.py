''' Print "Samad" four times '''

count = 0
def func():
    global count
    if count == 4:
        return
    print("Samad")
    count += 1
    func()
func()




