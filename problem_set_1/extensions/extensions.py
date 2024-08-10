z = input("File name: ").lower()
z = z.replace(" ", "")

filetype = z[z.rfind(".")+1:]

match filetype:
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case "pdf":
        print("application/pdf")
    case _:
        print("application/octet-stream")
