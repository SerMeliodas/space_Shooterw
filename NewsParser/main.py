import NewsParser as np
import api_layer as al

def main():
    content = np.main()
    print(al.Api().save(content))

if __name__ == '__main__':
    main()