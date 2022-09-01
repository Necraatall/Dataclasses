import inspect
from dataclasses import dataclass, astuple, asdict

@dataclass(order=True)
class Comment:
    id: int
    text: str

def main():
    comment = Comment(1, "I just subscriebed")
    print(comment)
    # print(astuple(comment))
    # print(asdict(comment))
    print(inspect.getmembers(comment, inspect.isfunction))

if __name__ == "__main__":
    main()
    Comment.id = 3
