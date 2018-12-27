 # coding: utf-8
 
'''
Question statement:
Given a list of project and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent on the first), 
determine a build order which allows the projects to be built. 
All of the project’s dependencies must be built before the project is. 
If there is no build order, your code must indicate so, but how you choose to do this is left open.

Input:
Projects: a, b, c, d, e, f
Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output:
	f, e, a, b, d, c
'''

class project:
	def __init__(self, name):
		self.project_name = name
		self.parent = []
		self.child = []

	def add_parent(self, parent_project):
		self.parent.append(parent_project)

	def add_child(self, child_project):
		self.child.append(child_project)

	def remove_parent(self, parent):
		self.parent.remove(parent)

def decide_order(projects, dependencies):
	for de in dependencies:
		de[0].add_child(de[1])
		de[1].add_parent(de[0])

	dummy = projects[0]
	while projects:
		if not dummy.parent:
			print(dummy.project_name)
			for ch in dummy.child:
				ch.remove_parent(dummy)
			projects.remove(dummy)
			if dummy.child:
				dummy = dummy.child[0]
			else:
				if projects:
					dummy = projects[0]
		else:
			dummy = dummy.parent[0]
			
if __name__ == '__main__':
	a = project('a')
	b = project('b')
	c = project('c')
	d = project('d')
	e = project('e')
	f = project('f')

	projects = [a, b, c, d, e, f]
	dependencies = [(a, d), (f, b), (b, d), (f, a), (d, c)]

	decide_order(projects, dependencies)

