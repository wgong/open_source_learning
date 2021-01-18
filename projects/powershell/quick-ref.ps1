# Powershell Lang Ref - C:\users\19197\zapme\Learn\Powershell
# Powershell cheatsheet - https://www.comparitech.com/net-admin/powershell-cheat-sheet/

“abcde” -replace “bc”, “TEST” 
# aTESTde

"abcde" -match "xyz"
# False

"abcde" -match "bc"
# True

"abcde" -match "BC"
# True

"abcde", "bc" -contains "BC"
# True

"data.csv" -like "*.csv"

"data.csv" -like "*.csv"
# true

# Each PowerShell Operator has a case sensitive version, prefixing any operator with c will make it case sensitive
"data.csv" -cmatch "^.*.CSV"
# false

$matched = "The number 7 is great!" -Match "\d"
$Matches.Count  # 1
$matches[0]
# 7

$matched = "The number 7 is great!" -Match "(\d)"
$Matches.Count  # 2
$matches[1]
# 7

## Powershell RegEx
- https://social.technet.microsoft.com/wiki/contents/articles/4310.powershell-working-with-regular-expressions-regex.aspx#:~:text=Case%20Sensitive%20Matching%20Each%20PowerShell%20Operator%20has%20a,people%20use%20it%20for%20cleaner%20more%20descriptive%20code.

"Hello Justin, Welcome" -match "hello\s(\w+), welcome"
"My name is $($matches[1])"

"hello world" -replace "world", "WORLD"
# hello WORLD

"today is 04/13/1999" -replace "\d{2}/\d{2}/\d{4}", (get-date -f "MM/dd/yyyy")

"today is $(get-date)"
# "today is $(get-date)"


"justin.rich@technet.com" -replace "^(\w+)\.(\w+)@", '$1_$2@'

$email2 = "justin.rich@technet.com" -replace "^(\w+)\.(\w+)@.*$", '$1_$2@'


"jrich100532" -replace "(\d+)", "XYZ"
jrichXYZ

$arr = "a, b, c, x" -split "," | % {$_.trim()}
$arr -join ":"

$s = ( 0..10 | ? {$_*$_ -gt 3} | % {2*$_} ) ; $s

## list comprehension
- https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension)#PowerShell

1..10 | foreach {$_ * 5}

1..10 | % {$_ * 5}

$s = 123 -as [string]

$s -is [int] # false
$s -is [string] # true


1..10 | foreach { "{0:N2}" -f $_ }

[datetime]$birthday = "1/10/66"

$sb = Get-Process | Select –First 2

$arr = 1, (3..5), 100

$arr | % {write-host $_}

$procs = @(get-process | select -first 3)
$procs.gettype() # system.array

# reverse an array

$arr=1..10
$arr2 = $arr[($arr.length-1)..0]
$arr3 = $arr + $arr2

$hash = @{"k91"="v1"; "k2"="v2" }
$hash2 = $hash.GetEnumerator() | sort Key

<# 
This is
A multi-line comment 
#>

$a = Get-Date
$a | Get-Member –MemberType Property
$a.Date
$a.TimeOfDay.Hours
$a | Get-Member -MemberType Property –Static

# access Static properties with :: operator
$a::now, $a::Today, $a::UtcNow

Monday, January 18, 2021 1:49:59 PM
Monday, January 18, 2021 12:00:00 AM
Monday, January 18, 2021 6:49:59 PM

$a = "  Hello Pwsh  "
$a | get-member -membertype Method
$a.ToLower().trim()

[String]::Equals("hello", " Hello ".trim().ToLower())
True

"This is a string, this $variable is expanded as is $(2+2)"
‘This is a string, $(2+2) is not expanded: ’
$big_str = @"
This is a here-string can contain anything including carriage
returns and quotes. Expressions are evaluated: $(2+2*5).
Note that the end marker of the here-string must be at the
beginning of a line!
"@

$str2 = @'
Here-strings with single quotes do not evaluate expressions:
$(2+2*5)
'@

$contents = @(Get-ChildItem ${env:ProgramFiles(x86)})
$contents | foreach {$_.Name}

# attributes can be used on variables
[ValidateRange(1,10)][int]$number = 1
$number = 11 #returns an error

# flip variables
$a=1;$b=2; write-host "a,b=$a,$b"; $a,$b = $b,$a; write-host "a,b=$a,$b"

$a,$b,$c = 'a b c'.split()

# create Constant variable (cannot be overwritten)
Set-Variable -Name Pi -Value 3.14 -Option Constant

$Services = Get-Service
$Services.Where({$_.Status -eq ‘Stopped’}, 'First', 3).ForEach{$_.Name.ToUpper()}
$Services.ForEach{$_.Name.ToUpper()}

foreach ($f in (dir "c:\")) {$f.Name}

dir "c:\" | foreach {$_.Name}

Get-Process | Select-Object Name, Company 

Get-Process | Where-Object { $_.Name –eq "brave" } | Select-Object Name,VM,WS,@{Label="TotalMemory";Expression={$_.vm + $_.ws}} | select -first 5

@{
    PropertyName = 'Value'
    ListProperty = @(
        'ListEntry1'
        'ListEntry2'
    )
} | convertto-json -dept 100 > dict.json
