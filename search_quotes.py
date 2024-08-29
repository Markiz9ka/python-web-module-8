from models import Author, Quote

def search_by_name(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print(f"Author with name {name} not found.")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    for quote in quotes:
        print(quote.quote)

def main():
    while True:
        command = input("input command (name, tag, tags, exit): ")
        if command.startswith("name:"):
            name = command[len("name:"):].strip()
            search_by_name(name)
        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip()
            search_by_tags(tags)
        elif command == "exit":
            break
        else:
            print("unknown command.")

if __name__ == '__main__':
    main()
