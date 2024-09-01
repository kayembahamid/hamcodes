const OEA = {
    Teacher: 'Ham',
    NumTeacher: 20,
    "EngTeacher": function(){
        // teach afternoon class
    }
};
// dot notation
OEA.Teacher; // 'Value''
// bracket notation
OEA["EngTeacher"]; // [function]
// the dot doesn't work on string property
// OEA."EngTeacher"
// calling number
OEA.NumTeacher;
// using brackets 
OEA[NumTeacher];
 const variable = 'Teacher';

OEA.variable; // this gives us 'undefined' because it's looking for a property named 'variable' in our object

OEA[variable] //  this is equivalent to OEA['EngTeacher'] and returns 'Value!''"''"