import client as cl


def log_in_gui():
    while True:
        option = input("Log In (l) or Sign Up (s): ")
        if option not in ['l', 's']:
            print("Please enter 'l' for log-in and 's' for sign-up.")
            continue
        else:
            break

    if option == 'l':
        pass

    elif option == 's':
        while True:
            username = input('Username: ').replace(' ', '')
            password = input('Password: ').replace(' ', '')

            cl_resp = cl.sign_up(username, password)
            if cl_resp == '-1':
                print(f'The username {username} have been taken.\n')
                continue
            else:
                print(f'Successfully logged-in as {username}')
                return cl_resp


def main():
    try:
        print('Welcome to Chat-App')

        print()
        auth_user = log_in_gui()

    except KeyboardInterrupt:
        pass

    finally:
        print('\n\nClosing Chat-App...')
        cl.disconnect_from_server()


main()

# # # -------------------------------- post msg test --------------------------------
# m = {"sender_id": 1, "rcv_id": 2, "send_time": datetime.now().strftime(
#     "%m/%d/%Y, %H:%M:%S"), "message_content": "Hello World"}
# data_ = json.dumps(m)
# post_msg(data_)
# # input()
#
# # -------------------------------- signup test --------------------------------
# # sign_up('dtuser4', 'Jk3WnSu2')
#
# # -------------------------------- disconnect --------------------------------
# disconnect_from_server()
