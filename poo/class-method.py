class Example:

    def test(self):

        return 'Teste';

    @classmethod
    def hello(cls):

        print('Hello, world!');

    def __repr__(self):

        return 'This represents the class';

    def __str__(self):

        return 'This doens\'t represent the class';

if __name__ == '__main__':
    
    example = Example();

    print(example);
    #print(Example.hello())
    print(example.test());
