const process = require("./fizzbuzz")

test("multiple of 3", () => {
    expect(process(6)).toBe("fizz")
})

test("multiple of 5", () => {
    expect(process(10)).toBe("buzz")
})

test("multiple of 3 and 5", () => {
    expect(process(15)).toBe("fizzbuzz")
})
