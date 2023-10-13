def main():
    msg = input()
    results =convert(msg)
    print(results)
def convert(msg):
    msg1=msg.replace (":)",'🙂')
    msg2=msg1.replace (":(", '🙁')
    return msg2
main()