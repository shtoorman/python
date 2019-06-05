import sys

print('версия Python {}.{}.{} на платформе {}'. \
      format(sys.version_info.major, sys.version_info.minor, \
             sys.version_info.micro, sys.platform))

first = True
switch = True
while (True):
    try:
        print('интервал *checkinterval : {} '.format(sys.getcheckinterval()))
        print('интервал *switchinterval : {} сек.'.format(sys.getswitchinterval()))
    except AttributeError:
        if first: print('*switchinterval не реализованы в этой версии Python');
        switch = False
    else:
        if first:
            print('*checkinterval объявлено устаревшими в этой версии Python')
    first = False
    while (True):
        try:
            val = int(input('введите checkinterval : ')); break;
        except ValueError:
            print('checkinterval должно быть целочисленным')
        except KeyboardInterrupt:
            print(); sys.exit(0)
    sys.setcheckinterval(val)
    if not switch: continue
    while (True):
        try:
            val = float(input('введите switchinterval : ')); break;
        except ValueError:
            print('switchinterval должно быть вещественным')
        except KeyboardInterrupt:
            print(); sys.exit(0)
    sys.setswitchinterval(val)
