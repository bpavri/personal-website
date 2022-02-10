from api import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# thislist = ["apple", "banana", "cherry", "strawberry", "grapes"]

# for (index, fruit) in enumerate(thislist):
#     if fruit == "banana":
#         print('popping '+index)
#         thislist.pop(index)
    
#     print(index)
#     print(fruit)

# print(thislist)