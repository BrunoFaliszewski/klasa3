# porządkowanie alfabetyczne

# https://appdividend.com/2021/06/02/how-to-sort-list-alphabetically-in-python/

if __name__ == '__main__':
    data = ['Elle', 'Miles', 'Kratos', 'Joel', 'Peter', 'Nathan']

    data.sort()
    print(data)

    data = ['Elle', 'Miles', 'Kratos', 'Joel', 'Peter', 'Nathan']

    print(sorted(data))

    data = ['Elle', 'miles', 'kratos', 'Joel', 'peter', 'Nathan']

    print(sorted(data))

    data = ['Elle', 'miles', 'kratos', 'Joel', 'peter', 'Nathan']

    print(sorted(data, key=str.lower))

    data = ['Elle', 'miles', 'kratos', 'Joel', 'peter', 'Nathan']

    print(sorted(data, reverse=True))