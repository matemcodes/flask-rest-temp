from models.example import Example, db

def get_all_example():
    examples = Example.query.all()
    return [example.message for example in examples]

def create_new_example(args):
    example = Example(message=args['message'])
    db.session.add(example); db.session.commit()
    return f"New example created: {example.message}"