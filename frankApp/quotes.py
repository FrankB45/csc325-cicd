import random

def random_quote():
    """
    Returns a random quote from a predefined list of quotes
    from famous programmers and computer scientists.
    """

    quotes = [
        "There are two ways to write error-free programs; only the third one works. - Alan Perlis",

        "Syntactic sugar causes cancer of the semi-colons. - Alan Perlis",

        "Three great virtues of programming are laziness, impatience, and hubris. - Larry Wall",

        "There are only two kinds of languages: the ones people complain about and the ones nobody uses. - Bjarne Stroustrup",

        "When in doubt, use brute force. - Ken Thompson",

        "I'd spell creat with an e. - Ken Thompson",

        "Object-oriented design is the roman numerals of computing. - Rob Pike",

        "C is quirky, flawed, and an enormous success. - Dennis Ritchie",

        "Bad programmers worry about the code. Good programmers worry about data structures and their relationships. - Linus Torvalds",

        "If you need more than 3 levels of indentation, you're screwed anyway, and should fix your program. - Linus Torvalds",

        "Beware of bugs in the above code; I have only proved it correct, not tried it. - Donald Knuth",

        "Premature optimization is the root of all evil. - Donald Knuth",

        "The most effective debugging tool is still careful thought, coupled with judiciously placed print statements. - Brian Kernighan",

        "Controlling complexity is the essence of computer programming. - Brian Kernighan",

        "It's easier to ask forgiveness than it is to get permission. - Grace Hopper",

        "The computer revolution hasn't started yet. - Alan Kay",

        "A change in perspective is worth 80 IQ points. - Alan Kay",

        "Testing shows the presence, not the absence of bugs. - Edsger Dijkstra",

        "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable. - Leslie Lamport",

        "Adding manpower to a late software project makes it later. - Frederick P. Brooks Jr.",

        "Plan to throw one away; you will, anyhow. - Frederick P. Brooks Jr.",

        "There are only two hard things in Computer Science: cache invalidation and naming things. - Phil Karlton",

        "Hofstadter's Law: It always takes longer than you expect, even when you take into account Hofstadter's Law. - Douglas Hofstadter",

        "I just had to take the hypertext idea and connect it to the TCP and DNS ideas and -- ta-da! -- the World Wide Web. - Tim Berners-Lee",

        "Java is C++ without the guns, knives, and clubs. - James Gosling",

        "Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' Now they have two problems. - Jamie Zawinski",

        "When there's a will to fail, obstacles can be found. - John McCarthy",

        "The nice thing about standards is that you have so many to choose from. - Andrew S. Tanenbaum",

        "Any sufficiently complicated C or Fortran program contains an ad hoc, informally specified, bug-ridden, slow implementation of half of Common Lisp. - Philip Greenspun",

        "Namespaces are one honking great idea -- let's do more of those! - Tim Peters",

        "If the implementation is hard to explain, it's a bad idea. - Tim Peters",

        "It's harder to read code than to write it. - Joel Spolsky",

        "A programming language is for thinking of programs, not for expressing programs you've already thought of. - Paul Graham",

        "The best code is no code at all. - Jeff Atwood",

        "Given enough eyeballs, all bugs are shallow. - Eric S. Raymond",

        "Programming languages are like cats. It is easier to get a new cat than to get an old cat fixed. - Douglas Crockford",

        "The speed of light sucks. - John Carmack",

        "I'm not a great programmer; I'm just a good programmer with great habits. - Kent Beck",

        "Good programmers value code that is easy to understand, and thus cheap to use and modify. - Martin Fowler",

        "Machines take me by surprise with great frequency. - Alan Turing",

        "Any problem in computer science can be solved with another layer of indirection. - David J. Wheeler",

        "The best way to prepare is to write programs, and to study great programs that other people have written. - Bill Gates",

        "The cheapest, fastest, and most reliable components are those that aren't there. - Gordon Bell",

        "Duplication is far cheaper than the wrong abstraction. - Sandi Metz",

        "The most profound technologies are those that disappear. - Mark Weiser",

        "Software gets slower faster than hardware gets faster. - Niklaus Wirth",

        "To iterate is human, to recurse divine. - L. Peter Deutsch",

        "Those who do not understand Unix are condemned to reinvent it, poorly. - Henry Spencer",

        "Walking on water and developing software from a specification are easy if both are frozen. - Edward V. Berard",

        "Free software is a matter of liberty, not price. - Richard Stallman",

        "The price of reliability is the pursuit of the utmost simplicity. - C. A. R. Hoare",

        "The only way to go fast, is to go well. - Robert C. Martin",

        "The greatest performance improvement of all is when a system goes from not-working to working. - John Ousterhout",

        "JavaScript is the world's most misunderstood programming language. - Douglas Crockford",
    ]

    return random.choice(quotes)