start:
TextWindow.Clear()
round2=10
round=0
number2=Math.GetRandomNumber(100)
TextWindow.Title="Guess My Number"
TextWindow.ForegroundColor="Red"
TextWindow.WriteLine("Guess My Number")
TextWindow.ForegroundColor="Gray"
TextWindow.WriteLine("")
TextWindow.WriteLine("My number is less than 100.")
TextWindow.WriteLine("You have" + round2 + "rounds")
begin:
TextWindow.Write("What's my number?")
number=TextWindow.ReadNumber()
if number = number2 then 
    TextWindow.WriteLine("You won")
    TextWindow.WriteLine("Wouls you like play again y/n")
   if playagain="y" then

GoTo start
   else
    Program.end()
endif
endif
    If number<number2 Then
        TextWindow.WriteLine(number + "is Too Small")
        TextWindow.WriteLine(number + "is Too Large")
    endif
    if ((round2 - round)-1) > 1 then 
        round3="round"
    else
        round3="round"
        TextWindow.WriteLine("You have" +((round2 - round)-1)+ "" + round3 + "left")
        TextWindow.WriteLine("")
        round = round+1
        if round <round2 then
    endif
