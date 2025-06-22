% This script estimates the Darcy friction factor using an iterative method.
% It repeatedly improves a guess until it converges to an accurate solution.

Re = 1e4;           % Reynolds number (represents flow conditions)
tol = 1e-8;         % Tolerance for stopping the loop (how accurate we want the result)

o(1) = 0.001;       % Initial guess for the friction factor
o(2) = iterate(Re, o(1));         % First refined guess using the formula
err(1) = abs(o(2) - o(1));        % Calculate the difference between the two guesses

i = 1;              % Iteration counter
max_iter = 1000;    % Safety limit: don't run more than 1000 times

% Keep improving the guess until it's accurate enough or we hit max_iter
while err(i) > tol && i < max_iter
    o(i+2) = iterate(Re, o(i+1));             % Generate new guess
    err(i+1) = abs(o(i+2) - o(i+1));          % Calculate how much it changed
    i = i + 1;                                % Go to the next iteration
end

x = o(end);         % Final estimated friction factor

% Display results
fprintf('Final friction factor: %.6f\n', x);
fprintf('Iterations: %d\n', i);

% Function that refines the guess using a formula related to fluid flow
function phi = iterate(Re, o)
    phi = (2.5 * log10(Re * o^(-0.5)) + 0.3)^(-2);
end
