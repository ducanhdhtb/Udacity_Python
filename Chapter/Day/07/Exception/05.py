# O Error - File Cannot Be Opened:

# try:
#     file = open("non_existent_file.txt", "r")
# except OSError as e:
#     print("An error occurred:", e)


# 1 ImportError - Module Not Found:
# try:
#     import non_existent_module
# except ImportError as e:
#     print("An error occurred:", e)

# ValueError - Inappropriate Value:
# try:
#     number = int("abc")
# except ValueError as e:
#     print("An error occurred:", e)


# KeyboardInterrupt - User Hits Interrupt Key:
try:
    while True:
        pass
except KeyboardInterrupt:
    print("User interrupted the program.")
