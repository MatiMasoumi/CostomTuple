from typing import Iterable


class CustomTuple(tuple):
    def __new__(cls,*args):

        unique_elements=tuple(sorted(set(args)))
        return super().__new__(cls,unique_elements)
    def add_(self,other):
        if isinstance(other,tuple):
            combined=CustomTuple(*(self + other))
            print(f"Tuples combined:{combined}")
            return combined
        else:
            raise TypeError('only tupels can be margen with a customTuple.')
    def sum(self):
        return sum(x for x in self if isinstance(x, (int,float)))
if __name__ == '__main__':
    t1 = CustomTuple(1,2,3,4)
    t2=CustomTuple(3,4,5,6)


    t3=t1.add_(t2)

    print('sum of elements in t3:', t3.sum())