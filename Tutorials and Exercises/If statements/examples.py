# ifstatements

is_hot = False
is_cold = True

if is_hot:
    print("hot day")
elif is_cold:
    print('cold day')
else:
    print('beatiful day')

if is_cold and not is_hot:
    print('ishotandnotcold')
