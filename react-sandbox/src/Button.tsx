import React from "react"
type ButtonProps = React.ComponentPropsWithoutRef<"button">
   & {
    variant?: "primary" | "secondary";
   }
;
const convertToArray = <T,>(value: T): T[] => {
    return [value];
}

export function Button(
    {type, autoFocus, variant, ...rest}: ButtonProps, 

){
    return <button type={type} autoFocus={autoFocus} {...rest}> Click me! </button>
}