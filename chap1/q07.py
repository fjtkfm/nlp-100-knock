# coding: utf-8

template = '%s時の%sは%s'


def return_template(x, y, z):
	return template % (str(x), str(y), str(z))

print(return_template(12, '気温', 22.4))
