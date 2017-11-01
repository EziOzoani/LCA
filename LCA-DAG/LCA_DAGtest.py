import LCA_DAG
import unittest
 
 
class MyTestCase(unittest.TestCase):
 
    def testStandard(self):
        root = LCA_DAG.Node(1)
        root.left = LCA_DAG.Node(2)
        root.right = LCA_DAG.Node(3)
        root.left.left = LCA_DAG.Node(4)
        root.left.right = LCA_DAG.Node(5)
        root.right.left = LCA_DAG.Node(6)
        root.right.right = LCA_DAG.Node(7)
        self.assertEqual(2,LCA_DAG.findLCA_DAG(root, 4, 5, ))
 
    def test2Nodes(self):
        root = LCA_DAG.Node(1)
        root.left = LCA_DAG.Node(2)
        self.assertEqual(1,LCA_DAG.findLCA_DAG(root, 1, 2, ))
 
 
 
    def testEmpty(self):
        self.assertEqual(-1,LCA_DAG.findLCA_DAG(None, None, None, ))
 
    def testNotPath(self):
        root = LCA_DAG.Node(1)
        root.left = LCA_DAG.Node(2)
        root.right = LCA_DAG.Node(3)
        root.left.left = LCA_DAG.Node(4)
        self.assertEqual(-1, LCA_DAG.findLCA_DAG(root, 2, 9, ))
 
 
 
if __name__ == '__main__':
    unittest.main()