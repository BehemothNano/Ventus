# Welcome to VentusExpress.
This is a fast language for creating easily interpretable data structures without having to have all parts of them.
In other words, VentusExpress or VTSX allows the storage of data in small files external to programs with a loose, non-sql like format, wherein there is no strict organizational structure, and data can just "thrown in" per se. This allows the usage and conversion of the data to supported languages such that things that should persist may remain. This is not intended to be used as a database, though it theoretically could be.

## Other things:
You'll notice that there are two ways of starting a data structure declaration in VTSX - "loose", or "strict". Each has advantages, for example, loose allows a declaration such as the following for a map (considered to be different to dictionaries):

    loose def map :: flightmap:
        --map assemblyAgent = "./flightmanager.py"
        --map cols.nameStruct:
            0 > sequential int LITERAL UNDEFINED
        --map rows.nameStruct:
            0 > sequential int LITERAL UNDEFINED
        // Do not write anything between lines 9 and whatever line "--map filepos.endStorageRegion()" is on.
        -- map filepos.beginStorageRegion(vtsx.anchor(9))
        |
        |
        |
        |
        |
        |
        |
        |
        --map filepos.endStorageRegion()

    vtsExpress.relegateSubprocesses(assemblyAgent)

Notice the use of the | character. It is considered a structural character when isolated, and will not be considered as carrying any meaning. This means that files can be organized with them such that the data defined by the declaration takes the place of the series of "|" characters. This is really just a way of showing where things will go even if they haven't been filled in yet.
Other things of importance are anchors, begin/end storage regions, and the last line,
    vtsExpress.relegateSubprocesses(assemblyAgent)
The first two allow the user to define where the data is actually stored. 
    filepos.beginStorageRegion(anchor)
Takes an anchor 
    vtsx.anchor(lineNum)
where lineNum refers to the line the anchor is on. In the above code, 
    --map filepos.beginStorageRegion(vtsx.anchor(9))
denotes that the map's storage region starts on line nine. However, this could instead be
    --map filepos.beginStorageRegion(vtxs.anchor(5000))
which would make the storage region start on line 5000 instead of the line directly after the *beginStorageRegion*. 
    --map filepos.endStorageRegion()
just needs to come after the *beginStorageRegion* line, but doesn't need an anchor. It can be given an anchor such that the data is given a concrete position in the file as opposed to a flexible one as is done above. In other words, a flexible position means that the data can use as many lines as it wants, which will make it nicely arranged. If it's forced between two lines, it'll just conform to that specification. However, using a flexible position is recommended, as one of the main advantages to storing data using VentusExpress is being able to see both the data, and how it is structured/what attributes it has, all in one place.

Going back to the last line,
    vtsExpress.relegateSubprocesses(assemblyAgent)
we can see that VTSX is relegating the task of actually assembling this object to another file, *"./flightmanager.py"* in the line
    --map assemblyAgent = "./flightmanager.py"
This means that VTSX isn't actually computing anything, but is instead just defining the structure of a data type to be used in that file. Since it's a Python file, it'll be done with the following code:
    from vtsx import vtsExpress
    ...

    ...
    flightmap = vtsExpress.retrieve(map, "flightmap")
This flightmap map could also be updated with the following:
    vtsExpress.update(map, "flightmap", flightmap)
Or deleted with:
    vtsExpress.drop(map, "flightmap", rmDef=0)
where *map* is the **data type**, *"flightmap"* is the **name** of the map, and *flightmap* is the **current value** the flightmap object holds, and is what will be put into the .vtsx file in place of the current "flightmap" map there. In the case of 
    vtsExpress.drop()
*rmDef* should either be *true* or *false* (defaults to *false*), as it declares whether or not VentusExpress should also delete the object definition. It defaults to false as the user may want to just delete the data stored there, but wants to keep the structure to fill with more data later. To fully remove the data and it's definition, simply set *rmDef* to *True*.


Every structure has attributes, similar to columns in a SQL database. Not all of these need to be used, and if they aren't specified, the user can either decide to use the default value, or to force all undefined attributes to a single value with the useage of:
    --datatype vtsx.udas : VALUE
For example, using the conformity statment above with the map example, 

----------------
This file is part of VentusExpress.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the software nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED ''AS IS'' AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.