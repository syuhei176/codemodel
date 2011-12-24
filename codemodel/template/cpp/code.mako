/*
 Copyright(C) Hiya Syuhei. 2011. All rights reserved.
*/

${root.name}::${root.name}()
{

}

${root.name}::~${root.name}()
{

}

<%namespace file="as.mako" import="*"/>
##${Compile(root.statemachine.states[i].code, ci)}\

