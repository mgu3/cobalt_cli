def keys(args, global_values):
    """ Entry point for commands that start 'cobalt-cli keys' """

    from cobalt_cli import option_is

    print("keys")

    print(args)
    print(global_values)

    if option_is(args, "notifications_file_upload"):
        print("Upload file now")
