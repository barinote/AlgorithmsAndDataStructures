from binaryTree import BinaryTree
from heap import Heap
import operator
import copy


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Heap()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def cleanFractions(parseTree, _var='x'):

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if parseTree.getRootVal() == '/':
        if leftC.getRootVal() == _var and rightC.getRootVal() == _var:
            return BinaryTree('1')
        elif leftC.getRootVal() == _var and rightC.getRootVal() == '*':
            rr = rightC.getRightChild()
            ll = rightC.getLeftChild()
            if rr.getRootVal() == _var:
                rr.key = '1'
                leftC.key = '1'
            elif ll.getRootVal() == _var:
                ll.key = '1'
                leftC.key = '1'
        elif leftC.getRootVal() == '*' and rightC.getRootVal() == _var:
            rr = leftC.getRightChild()
            ll = leftC.getLeftChild()
            if rr.getRootVal() == _var:
                rr.key = '1'
                rightC.key = '1'
            elif ll.getRootVal() == _var:
                ll.key = '1'
                rightC.key = '1'
        elif leftC.getRootVal() == '*' and rightC.getRootVal() == '*':
            llr = leftC.getRightChild()
            lll = leftC.getLeftChild()

            rrr = rightC.getRightChild()
            rrl = rightC.getLeftChild()

            if llr.getRootVal() == _var and rrr.getRootVal() == _var:
                llr.key = '1'
                rrr.key = '1'
            elif llr.getRootVal() == _var and rrl.getRootVal() == _var:
                llr.key = '1'
                rrl.key = '1'
            elif lll.getRootVal() == _var and rrl.getRootVal() == _var:
                lll.key = '1'
                rrl.key = '1'
            elif lll.getRootVal() == _var and rrr.getRootVal() == _var:
                lll.key = '1'
                rrr.key = '1'

    elif leftC.getRootVal() in ['+', '-', '*']:
        cleanFractions(leftC)
    elif rightC.getRootVal() in ['+', '-', '*']:
        cleanFractions(rightC)

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub,
             '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def derivative(parseTree, _var='x'):

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if parseTree.getRootVal() in ['+', '-']:
        parseTree.leftChild = derivative(leftC)
        parseTree.rightChild =  derivative(rightC)

    elif parseTree.getRootVal() == '*':
        t = BinaryTree('+')

        L = BinaryTree('*')
        R = BinaryTree('*')

        tmpl = copy.copy(leftC)
        tmpr = copy.copy(rightC)

        L.leftChild = (leftC)
        L.rightChild = (derivative(tmpr))

        R.leftChild = (derivative(tmpl))
        R.rightChild = (rightC)

        t.leftChild = L
        t.rightChild = R

        return t

    elif parseTree.getRootVal() == '/':
        node = BinaryTree('-')

        frac1 = BinaryTree('/')
        frac2 = BinaryTree('/')

        frac2count = BinaryTree('*')
        frac2denom = BinaryTree('*')

        node.leftChild = frac1
        node.rightChild = frac2

        frac1.leftChild = derivative(leftC)
        frac1.rightChild = rightC

        frac2.leftChild = frac2count
        frac2.rightChild = frac2denom

        frac2denom.leftChild = rightC
        frac2denom.rightChild = rightC

        tmpr = copy.copy(rightC)
        frac2count.leftChild = derivative(tmpr)
        frac2count.rightChild = leftC

        return node

    elif parseTree.getRootVal() == _var:
        return BinaryTree('1')
    else:
        return BinaryTree('0')

    return parseTree


def cleaner(parseTree, _var='x'):

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC.getRootVal() in ['+', '-', '/', '*']:
        parseTree.leftChild = cleaner(leftC)
    if rightC.getRootVal() in ['+', '-', '/', '*']:
        parseTree.rightChild = cleaner(rightC)

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    rootval = parseTree.getRootVal()
    lval = leftC.getRootVal()
    rval = rightC.getRootVal()

    try:
        lval = float(lval)
    except: pass
    #print(lval)

    try:
        rval = float(rval)
    except: pass
    #print(rval)

    areNumbers = (isinstance(lval, float) and isinstance(rval, float))

    if (rootval == '*' or rootval == '/') and (lval == 0 or rval == 0):
        return BinaryTree('0')
    elif rootval == '*' and lval == 1:
        return rightC
    elif rootval == '*' and rval == 1:
        return leftC
    elif rootval == '/' and rval == 1:
        return leftC
    elif rootval == '+' and (lval == _var and rval == _var):
        return BinaryTree('2x')
    elif rootval == '*' and (isinstance(lval, float) and rval == _var):
        mul = str(lval) + _var
        return BinaryTree(mul)
    elif rootval == '*' and (isinstance(rval, float) and lval == _var):
        mul = str(rval) + _var
        return BinaryTree(mul)
    elif rootval == '*' and areNumbers:
        return BinaryTree(str(lval*rval))
    elif rootval == '/' and areNumbers:
        return BinaryTree(str(lval/rval))
    elif rootval == '+' and areNumbers:
        return BinaryTree(str(lval+rval))
    elif rootval == '-' and areNumbers:
        return BinaryTree(str(lval-rval))

    return parseTree


if __name__ == '__main__':
    pt = buildParseTree("( x *  x )")

    cleanFractions(pt)
    der = derivative(pt)
    print(printexp(der))
    print(printexp(cleaner(der)))



