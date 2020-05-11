from collections import namedtuple
Task = namedtuple(
    'Task', ['Summary', 'Owner', 'done', 'ID']
    )
Task.__new__.__defaults__ = (None, None, False, None)
# print(Task)

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2 

def test_member_access():
    """Check field functionality of namedtuple"""
    t = Task('buy milk', 'brian')
    assert t.Summary == 'buy milk'
    assert t.Owner == 'brian'
    assert (t.done, t.ID) == (False, None)
