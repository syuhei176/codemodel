/*
 * (C) Copyright 2010-2011 Syuhei Hiya. All rights reserved.
 */
class ${root.name};
#ifndef __${root.name}_H
#define __${root.name}_H

class ${root.name} {
%for property in root.properties:
	${property.type} ${property.name};
%endfor

	${root.name}();
	~${root.name}();
%for operation in root.operations:
	${operation.type} ${operation.name}();
%endfor

};

#endif /* __${root.name}_H */
