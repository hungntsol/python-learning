import b
print(f"before import b")


print(f"before main executed: {__name__}")

if __name__ == "__main__":
    print(f"main executed: {__name__}")

if __name__ == "b":
    print("execute main in b")
