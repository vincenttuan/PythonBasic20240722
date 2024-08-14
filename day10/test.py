x = True
y = False
z = False
if not x or y:  # not x 是 False or y 是 False
    print(1)
elif not x or not y and z:  # not x 是 False or not y 是 True and z 是 False
                            # False or True and False
                            # False or False
                            # False
    print(2)
elif not x or y or not y and x:  # not x 是 False or y 是 False or not y 是 True and x 是 True
                                 # not x 是 False or y 是 False or True
                                 # False or False or True
                                 # False or True
                                 # True
    print(3)
else:
    print(4)