
def inflate_tag(tag, namespaces):
	if ':' in tag:
		ns, _tag = tag.split(':')
		tag = '{{{namespace}}}{tag}'.format(
			namespace=namespaces[ns],
			tag=_tag
		)
	return tag
