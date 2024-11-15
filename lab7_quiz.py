def rlen(items):
    count=0
    if items!=[]:
        count=1+rlen(items[1:])
    return count


if __name__ == "__main__":
    print(rlen([1,2]))