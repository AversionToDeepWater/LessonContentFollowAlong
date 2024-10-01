def division(num, divide_by):
    return num / divide_by

# division(6, 0) ## Boom...

def handling_exception():
    try:
        ## Try and run our function.
        division(10,5 )
    except:
        ## We can now safely control our exception boom.
        return 0
    else:
        ## Run on success, after the Try body.
        print('This is because it worked.')
    finally:
        ## Always run.
        print('I run, rain or shine, success or failure.')

handling_exception()