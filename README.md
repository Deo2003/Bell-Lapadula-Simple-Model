# Bell-Lapadula-Simple-Model
A basic implementation of the Bell-LaPadula (BLP) Model in Python. 

This model enforces mandatory access control based on security levels to maintain confidentiality. The two key properties are:

Simple Security Property ("No Read Up" - NRU): A subject at a lower security level cannot read data at a higher security level.
*-Property ("No Write Down" - NWD): A subject at a higher security level cannot write data to a lower security level.
This implementation includes:

A Subject class (users/processes accessing data) </br>
An Object class (files/resources with security labels) </br>
An Access Control system that enforces Bell-LaPadula properties. </br>
