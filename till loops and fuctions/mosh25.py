# "**" is used when we want to print keywaord
# as well ex- code=234 will print 'code=' as
# well along with 2234
def products(**data):

    # here we're accessing quantity in the
    # data
    print(data["quantity"])


products(code=234, type="snacks", quantity=5)
