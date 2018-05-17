from tie import get_driver, vote

driver = get_driver()

while 1:
    try:
        vote(driver)
    except Exception as err:
        print(err)
