%{
Title: Synopsys Program
Author: Anthony Bruno

Description: This script performs the sequence a_n + a_(n+1) expression on
a squence of integers and produces a new sequence that is 1 term less than
the previous sequence. It continues this process until the final output
sequence length is 1 term. 

Example:
input = [1,2,3]
outputs: [3,5], [8]
%}

% ---------------- SETUPS & INITIALIZATIONS -----------------------

clear   % Clear the workspace data
clc     % clear the console window

input_array    = [4,7,3,6,7];          % <<<<<< INPUT ARRAY >>>>>>>
%input_array     = [1,2,3];


N               = length(input_array);  % N = length of the input array
Iterations      = N-1;                  % number of times to loop throughthe input array

current_array   = input_array;          % set the current array to input array (used for manipulation)


% PRINT INPUT ARRAY
fprintf('Input Array: [%s]\n', join(string(input_array),',')); % Prints out the input array to the console


% PRINT THE OUTPUT ARRAYS
for g=1:1:Iterations                        % Loop length(input array)-1 times
    current_array = myfunc(current_array);  % Call myfunc() on current array and 
                                            % return the resulting output array, set to current_array
end



% ----------------- FUNCTIONS ------------------------------
% Name: my_func
% input: array of integers
% Output/Return: array of integers with 1 element less than the input array
% of function

function output_arr = myfunc(array)                     % Name of function, its return array, and input array
    n = length(array);                                  % Get length of the array
    iter = n-1;                                         % Get the iterations from the array length
    output_arr = ones(1,iter);                          % Create an output array with 1 element less than array
    for i=1:1:iter                                      % Loop
        output_arr(i) = array(i) + array(i+1);          % Set the output array at index i to be the result of
                                                        % a_n + a_(n+1). 
    end
    fprintf('[%s]\n', join(string(output_arr),','));    % Print resulting output array to console
end


% MISC CODE (Ignore this)
% FOR DEBUGGING AS NEEDED
% fprintf('Output Array: [%s]\n', join(string(output_array),','));