def test_function():
    def inner_function():
        print("\n>>>---------<<<")
        print("Я в области видимости функции test_function")
        print(">>>---------<<<\n")
    inner_function()
test_function()
inner_function()
