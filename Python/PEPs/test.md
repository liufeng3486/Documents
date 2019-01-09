PEP 0 -- Python改进建议目录  (PEPs)   - 部分
=====================================================

|PEP编号:|0|
|:----|:----|
|标题:|Python改进建议目录 (PEPs)|
|原文地址:|https://www.python.org/dev/peps/|
|作者:|python-dev <python-dev at python.org>|
|状态:|Active|
|类型:|信息|
|创建时间:|13-Jul-2000|
* * *
### 内容
*   [介绍](#介绍)
*   [类别索引](#类别索引)
<div style="display:none;">
    *   [Meta-PEPs (PEPs about PEPs or Processes)](#meta-peps-peps-about-peps-or-processes)
    *   [Other Informational PEPs](#other-informational-peps)
    *   [Provisional PEPs (provisionally accepted; interface may still change)](#provisional-peps-provisionally-accepted-interface-may-still-change)
    *   [Accepted PEPs (accepted; may not be implemented yet)](#accepted-peps-accepted-may-not-be-implemented-yet)
    *   [Open PEPs (under consideration)](#open-peps-under-consideration)
    *   [Finished PEPs (done, with a stable interface)](#finished-peps-done-with-a-stable-interface)
    *   [Historical Meta-PEPs and Informational PEPs](#historical-meta-peps-and-informational-peps)
    *   [Deferred PEPs (postponed pending further research or updates)](#deferred-peps-postponed-pending-further-research-or-updates)
    *   [Abandoned, Withdrawn, and Rejected PEPs](#abandoned-withdrawn-and-rejected-peps)
*   [Numerical Index](#numerical-index)
*   [Reserved PEP Numbers](#reserved-pep-numbers)
*   [PEP Types Key](#pep-types-key)
*   [PEP Status Key](#pep-status-key)
*   [Authors/Owners](#authors-owners)
*   [References](#id1)
</div>
[介绍](#介绍)
====================
本PEP包含了所有Python改进建议的索引，即PEPs。PEP编号由PEP作者确定，该编号一旦分配，将永不更改\[[1](#id2)\]。所有历史记录与版本号相关联\[[2](#id3)\].

[类别索引](#类别索引)
=========================

[Meta-PEPs (不针对python，而是关于其周边的PEP)](#id6)
------------------------------------------------
|类型|PEP编号|标题|作者|原文地址|中文地址|
|:----|:----|:----|:----|:----|:----|
|P|[1](/dev/peps/pep-0001)|PEP 目的及指南 |Warsaw, Hylton, Goodger, Coghlan|[PEP Purpose and Guidelines](https://www.python.org/dev/peps/pep-0001/)||
|P|[4](/dev/peps/pep-0004)|反对旧版本|Cannon, von Löwis|
|P|[5](/dev/peps/pep-0005)|Guidelines for Language Evolution|Prescod|
|P|[6](/dev/peps/pep-0006)|Bug Fix Releases|Aahz, Baxter|
|P|[7](/dev/peps/pep-0007)|Style Guide for C Code|GvR, Warsaw|
|P|[8](/dev/peps/pep-0008)|Style Guide for Python Code|GvR, Warsaw, Coghlan|
|P|[10](/dev/peps/pep-0010)|Voting Guidelines|Warsaw|
|P|[11](/dev/peps/pep-0011)|Removing support for little used platforms|von Löwis, Cannon|
|P|[12](/dev/peps/pep-0012)|Sample reStructuredText PEP Template|Goodger, Warsaw|
|P|[573](/dev/peps/pep-0573)|Module State Access from C Extension Methods|Viktorin, Coghlan, Snow, Plch|

[Other Informational PEPs](#id7)
--------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|I|[13](/dev/peps/pep-0013)|Python Language Governance|and community|
|I|[20](/dev/peps/pep-0020)|The Zen of Python|Peters|
|I|[101](/dev/peps/pep-0101)|Doing Python Releases 101|Warsaw, GvR|
|IF|[247](/dev/peps/pep-0247)|API for Cryptographic Hash Functions|Kuchling|
|IF|[248](/dev/peps/pep-0248)|Python Database API Specification v1.0|Lemburg|
|IF|[249](/dev/peps/pep-0249)|Python Database API Specification v2.0|Lemburg|
|I|[257](/dev/peps/pep-0257)|Docstring Conventions|Goodger, GvR|
|IF|[272](/dev/peps/pep-0272)|API for Block Encryption Algorithms v1.0|Kuchling|
|I|[287](/dev/peps/pep-0287)|reStructuredText Docstring Format|Goodger|
|I|[290](/dev/peps/pep-0290)|Code Migration and Modernization|Hettinger|
|IF|[291](/dev/peps/pep-0291)|Backward Compatibility for the Python 2 Standard ...|Norwitz|
|IF|[333](/dev/peps/pep-0333)|Python Web Server Gateway Interface v1.0|Eby|
|I|[373](/dev/peps/pep-0373)|Python 2.7 Release Schedule|Peterson|
|I|[394](/dev/peps/pep-0394)|The "python" Command on Unix-Like Systems|Staley, Coghlan, Warsaw, Viktorin|
|IF|[399](/dev/peps/pep-0399)|Pure Python/C Accelerator Module Compatibility ...|Cannon|
|IF|[404](/dev/peps/pep-0404)|Python 2.8 Un-release Schedule|Warsaw|
|I|[411](/dev/peps/pep-0411)|Provisional packages in the Python standard library|Coghlan, Bendersky|
|I|[429](/dev/peps/pep-0429)|Python 3.4 Release Schedule|Hastings|
|IF|[430](/dev/peps/pep-0430)|Migrating to Python 3 as the default online ...|Coghlan|
|I|[434](/dev/peps/pep-0434)|IDLE Enhancement Exception for All Branches|Rovito, Reedy|
|I|[440](/dev/peps/pep-0440)|Version Identification and Dependency Specification|Coghlan, Stufft|
|I|[478](/dev/peps/pep-0478)|Python 3.5 Release Schedule|Hastings|
|I|[494](/dev/peps/pep-0494)|Python 3.6 Release Schedule|Deily|
|IA|[503](/dev/peps/pep-0503)|Simple Repository API|Stufft|
|I|[508](/dev/peps/pep-0508)|Dependency specification for Python Software Packages|Collins|
|I|[513](/dev/peps/pep-0513)|A Platform Tag for Portable Linux Built Distributions|McGibbon, Smith|
|I|[514](/dev/peps/pep-0514)|Python registration in the Windows registry|Dower|
|I|[537](/dev/peps/pep-0537)|Python 3.7 Release Schedule|Deily|
|I|[571](/dev/peps/pep-0571)|The manylinux2010 Platform Tag|Williams, Thomas, Kluyver|
|IF|[3333](/dev/peps/pep-3333)|Python Web Server Gateway Interface v1.0.1|Eby|
|I|[8000](/dev/peps/pep-8000)|Python Language Governance Proposal Overview|Warsaw|
|I|[8002](/dev/peps/pep-8002)|Open Source Governance Survey|Warsaw, Langa, Pitrou, Hellmann, Willing|
|IA|[8016](/dev/peps/pep-8016)|The Steering Council Model|Smith, Stufft|
|I|[8100](/dev/peps/pep-8100)|January 2019 steering council election|Smith, III|

[Provisional PEPs (provisionally accepted; interface may still change)](#id8)
----------------------------------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|SP|[484](/dev/peps/pep-0484)|Type Hints|GvR, Lehtosalo, Langa|
|SP|[517](/dev/peps/pep-0517)|A build-system independent format for source trees|Smith, Kluyver|
|SP|[518](/dev/peps/pep-0518)|Specifying Minimum Build System Requirements for ...|Cannon, Smith, Stufft|

[Accepted PEPs (accepted; may not be implemented yet)](#id9)
------------------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|SA|[557](/dev/peps/pep-0557)|Data Classes|Smith|
|SA|[560](/dev/peps/pep-0560)|Core support for typing module and generic types|Levkivskyi|
|SA|[561](/dev/peps/pep-0561)|Distributing and Packaging Type Information|Smith|
|SA|[563](/dev/peps/pep-0563)|Postponed Evaluation of Annotations|Langa|
|SA|[572](/dev/peps/pep-0572)|Assignment Expressions|Angelico, Peters, GvR|
|SA|[3121](/dev/peps/pep-3121)|Extension Module Initialization and Finalization|von Löwis|

[Open PEPs (under consideration)](#id10)
----------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|S|[381](/dev/peps/pep-0381)|Mirroring infrastructure for PyPI|Ziadé, v. Löwis|
|P|[387](/dev/peps/pep-0387)|Backwards Compatibility Policy|Peterson|
|S|[432](/dev/peps/pep-0432)|Restructuring the CPython startup sequence|Coghlan|
|S|[436](/dev/peps/pep-0436)|The Argument Clinic DSL|Hastings|
|S|[447](/dev/peps/pep-0447)|Add \_\_getdescriptor\_\_ method to metaclass|Oussoren|
|I|[452](/dev/peps/pep-0452)|API for Cryptographic Hash Functions v2.0|Kuchling, Heimes|
|I|[457](/dev/peps/pep-0457)|Syntax For Positional-Only Parameters|Hastings|
|S|[458](/dev/peps/pep-0458)|Surviving a Compromise of PyPI|Kuppusamy, Diaz, Stufft, Cappos|
|S|[467](/dev/peps/pep-0467)|Minor API improvements for binary sequences|Coghlan, Furman|
|S|[472](/dev/peps/pep-0472)|Support for indexing with keyword arguments|Borini, Martinot-Lagarde|
|S|[473](/dev/peps/pep-0473)|Adding structured data to built-in exceptions|Kreft|
|S|[480](/dev/peps/pep-0480)|Surviving a Compromise of PyPI: The Maximum ...|Kuppusamy, Diaz, Stufft, Cappos|
|I|[482](/dev/peps/pep-0482)|Literature Overview for Type Hints|Langa|
|I|[483](/dev/peps/pep-0483)|The Theory of Type Hints|GvR, Levkivskyi|
|S|[491](/dev/peps/pep-0491)|The Wheel Binary Package Format 1.9|Holth|
|P|[497](/dev/peps/pep-0497)|A standard mechanism for backward compatibility|Schofield|
|S|[499](/dev/peps/pep-0499)|python -m foo should bind ...|Simpson|
|I|[502](/dev/peps/pep-0502)|String Interpolation - Extended Discussion|Miller|
|S|[533](/dev/peps/pep-0533)|Deterministic cleanup for iterators|Smith|
|S|[534](/dev/peps/pep-0534)|Distributing a Subset of the Standard Library|Orsava, Viktorin, Coghlan|
|S|[536](/dev/peps/pep-0536)|Final Grammar for Literal String Interpolation|Angerer|
|S|[542](/dev/peps/pep-0542)|Dot Notation Assignment In Function Header|Meskanen|
|S|[543](/dev/peps/pep-0543)|A Unified TLS API for Python|Benfield, Heimes|
|S|[544](/dev/peps/pep-0544)|Protocols: Structural subtyping (static duck typing)|Levkivskyi, Lehtosalo, Langa|
|I|[551](/dev/peps/pep-0551)|Security transparency in the Python runtime|Dower|
|S|[554](/dev/peps/pep-0554)|Multiple Interpreters in the Stdlib|Snow|
|S|[556](/dev/peps/pep-0556)|Threaded garbage collection|Pitrou|
|S|[558](/dev/peps/pep-0558)|Defined semantics for locals()|Coghlan|
|I|[569](/dev/peps/pep-0569)|Python 3.8 Release Schedule|Langa|
|S|[570](/dev/peps/pep-0570)|Python Positional-Only Parameters|Hastings, Galindo, Corchero|
|S|[574](/dev/peps/pep-0574)|Pickle protocol 5 with out-of-band data|Pitrou|
|S|[576](/dev/peps/pep-0576)|Rationalize Built-in function classes|Shannon|
|S|[578](/dev/peps/pep-0578)|Python Runtime Audit Hooks|Dower|
|I|[579](/dev/peps/pep-0579)|Refactoring C functions and methods|Demeyer|
|S|[580](/dev/peps/pep-0580)|The C call protocol|Demeyer|
|P|[581](/dev/peps/pep-0581)|Using GitHub Issues for CPython|Wijaya|
|S|[582](/dev/peps/pep-0582)|Python local packages directory|Das, Dower, Stufft, Coghlan|
|I|[801](/dev/peps/pep-0801)|Reserved|Warsaw|
  
[Finished PEPs (done, with a stable interface)](#id11)
------------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|SF|[100](/dev/peps/pep-0100)|Python Unicode Integration|Lemburg|
|SF|[201](/dev/peps/pep-0201)|Lockstep Iteration|Warsaw|
|SF|[202](/dev/peps/pep-0202)|List Comprehensions|Warsaw|
|SF|[203](/dev/peps/pep-0203)|Augmented Assignments|Wouters|
|SF|[205](/dev/peps/pep-0205)|Weak References|Drake|
|SF|[207](/dev/peps/pep-0207)|Rich Comparisons|GvR, Ascher|
|SF|[208](/dev/peps/pep-0208)|Reworking the Coercion Model|Schemenauer, Lemburg|
|SF|[214](/dev/peps/pep-0214)|Extended Print Statement|Warsaw|
|SF|[217](/dev/peps/pep-0217)|Display Hook for Interactive Use|Zadka|
|SF|[218](/dev/peps/pep-0218)|Adding a Built-In Set Object Type|Wilson, Hettinger|
|SF|[221](/dev/peps/pep-0221)|Import As|Wouters|
|SF|[223](/dev/peps/pep-0223)|Change the Meaning of \x Escapes|Peters|
|SF|[227](/dev/peps/pep-0227)|Statically Nested Scopes|Hylton|
|SF|[229](/dev/peps/pep-0229)|Using Distutils to Build Python|Kuchling|
|SF|[230](/dev/peps/pep-0230)|Warning Framework|GvR|
|SF|[232](/dev/peps/pep-0232)|Function Attributes|Warsaw|
|SF|[234](/dev/peps/pep-0234)|Iterators|Yee, GvR|
|SF|[235](/dev/peps/pep-0235)|Import on Case-Insensitive Platforms|Peters|
|SF|[236](/dev/peps/pep-0236)|Back to the \_\_future\_\_|Peters|
|SF|[237](/dev/peps/pep-0237)|Unifying Long Integers and Integers|Zadka, GvR|
|SF|[238](/dev/peps/pep-0238)|Changing the Division Operator|Zadka, GvR|
|SF|[241](/dev/peps/pep-0241)|Metadata for Python Software Packages|Kuchling|
|SF|[250](/dev/peps/pep-0250)|Using site-packages on Windows|Moore|
|SF|[252](/dev/peps/pep-0252)|Making Types Look More Like Classes|GvR|
|SF|[253](/dev/peps/pep-0253)|Subtyping Built-in Types|GvR|
|SF|[255](/dev/peps/pep-0255)|Simple Generators|Schemenauer, Peters, Hetland|
|SF|[260](/dev/peps/pep-0260)|Simplify xrange()|GvR|
|SF|[261](/dev/peps/pep-0261)|Support for "wide" Unicode characters|Prescod|
|SF|[263](/dev/peps/pep-0263)|Defining Python Source Code Encodings|Lemburg, von Löwis|
|SF|[264](/dev/peps/pep-0264)|Future statements in simulated shells|Hudson|
|SF|[273](/dev/peps/pep-0273)|Import Modules from Zip Archives|Ahlstrom|
|SF|[274](/dev/peps/pep-0274)|Dict Comprehensions|Warsaw|
|SF|[277](/dev/peps/pep-0277)|Unicode file name support for Windows NT|Hodgson|
|SF|[278](/dev/peps/pep-0278)|Universal Newline Support|Jansen|
|SF|[279](/dev/peps/pep-0279)|The enumerate() built-in function|Hettinger|
|SF|[282](/dev/peps/pep-0282)|A Logging System|Sajip, Mick|
|SF|[285](/dev/peps/pep-0285)|Adding a bool type|GvR|
|SF|[289](/dev/peps/pep-0289)|Generator Expressions|Hettinger|
|SF|[292](/dev/peps/pep-0292)|Simpler String Substitutions|Warsaw|
|SF|[293](/dev/peps/pep-0293)|Codec Error Handling Callbacks|Dörwald|
|SF|[301](/dev/peps/pep-0301)|Package Index and Metadata for Distutils|Jones|
|SF|[302](/dev/peps/pep-0302)|New Import Hooks|JvR, Moore|
|SF|[305](/dev/peps/pep-0305)|CSV File API|Altis, Cole, McNamara, Montanaro, Wells|
|SF|[307](/dev/peps/pep-0307)|Extensions to the pickle protocol|GvR, Peters|
|SF|[308](/dev/peps/pep-0308)|Conditional Expressions|GvR, Hettinger|
|SF|[309](/dev/peps/pep-0309)|Partial Function Application|Harris|
|SF|[311](/dev/peps/pep-0311)|Simplified Global Interpreter Lock Acquisition for ...|Hammond|
|SF|[314](/dev/peps/pep-0314)|Metadata for Python Software Packages v1.1|Kuchling, Jones|
|SF|[318](/dev/peps/pep-0318)|Decorators for Functions and Methods|Smith|
|SF|[322](/dev/peps/pep-0322)|Reverse Iteration|Hettinger|
|SF|[324](/dev/peps/pep-0324)|subprocess - New process module|Astrand|
|SF|[327](/dev/peps/pep-0327)|Decimal Data Type|Batista|
|SF|[328](/dev/peps/pep-0328)|Imports: Multi-Line and Absolute/Relative|Aahz|
|SF|[331](/dev/peps/pep-0331)|Locale-Independent Float/String Conversions|Reis|
|SF|[338](/dev/peps/pep-0338)|Executing modules as scripts|Coghlan|
|SF|[341](/dev/peps/pep-0341)|Unifying try-except and try-finally|Brandl|
|SF|[342](/dev/peps/pep-0342)|Coroutines via Enhanced Generators|GvR, Eby|
|SF|[343](/dev/peps/pep-0343)|The "with" Statement|GvR, Coghlan|
|SF|[345](/dev/peps/pep-0345)|Metadata for Python Software Packages 1.2|Jones|
|SF|[352](/dev/peps/pep-0352)|Required Superclass for Exceptions|Cannon, GvR|
|SF|[353](/dev/peps/pep-0353)|Using ssize_t as the index type|von Löwis|
|SF|[357](/dev/peps/pep-0357)|Allowing Any Object to be Used for Slicing|Oliphant|
|SF|[358](/dev/peps/pep-0358)|The "bytes" Object|Schemenauer, GvR|
|SF|[362](/dev/peps/pep-0362)|Function Signature Object|Cannon, Seo, Selivanov, Hastings|
|SF|[366](/dev/peps/pep-0366)|Main module explicit relative imports|Coghlan|
|SF|[370](/dev/peps/pep-0370)|Per user site-packages directory|Heimes|
|SF|[371](/dev/peps/pep-0371)|Addition of the multiprocessing package to the ...|Noller, Oudkerk|
|SF|[372](/dev/peps/pep-0372)|Adding an ordered dictionary to collections|Ronacher, Hettinger|
|SF|[376](/dev/peps/pep-0376)|Database of Installed Python Distributions|Ziadé|
|SF|[378](/dev/peps/pep-0378)|Format Specifier for Thousands Separator|Hettinger|
|SF|[380](/dev/peps/pep-0380)|Syntax for Delegating to a Subgenerator|Ewing|
|SF|[383](/dev/peps/pep-0383)|Non-decodable Bytes in System Character Interfaces|v. Löwis|
|SF|[384](/dev/peps/pep-0384)|Defining a Stable ABI|v. Löwis|
|SF|[389](/dev/peps/pep-0389)|argparse - New Command Line Parsing Module|Bethard|
|SF|[391](/dev/peps/pep-0391)|Dictionary-Based Configuration For Logging|Sajip|
|SF|[393](/dev/peps/pep-0393)|Flexible String Representation|v. Löwis|
|SF|[397](/dev/peps/pep-0397)|Python launcher for Windows|Hammond, v. Löwis|
|SF|[405](/dev/peps/pep-0405)|Python Virtual Environments|Meyer|
|SF|[409](/dev/peps/pep-0409)|Suppressing exception context|Furman|
|SF|[412](/dev/peps/pep-0412)|Key-Sharing Dictionary|Shannon|
|SF|[414](/dev/peps/pep-0414)|Explicit Unicode Literal for Python 3.3|Ronacher, Coghlan|
|SF|[415](/dev/peps/pep-0415)|Implement context suppression with exception attributes|Peterson|
|SF|[417](/dev/peps/pep-0417)|Including mock in the Standard Library|Foord|
|SF|[418](/dev/peps/pep-0418)|Add monotonic time, performance counter, and ...|Simpson, Jewett, Turnbull, Stinner|
|SF|[420](/dev/peps/pep-0420)|Implicit Namespace Packages|Smith|
|SF|[421](/dev/peps/pep-0421)|Adding sys.implementation|Snow|
|SF|[424](/dev/peps/pep-0424)|A method for exposing a length hint|Gaynor|
|SF|[425](/dev/peps/pep-0425)|Compatibility Tags for Built Distributions|Holth|
|SF|[427](/dev/peps/pep-0427)|The Wheel Binary Package Format 1.0|Holth|
|SF|[428](/dev/peps/pep-0428)|The pathlib module -- object-oriented filesystem paths|Pitrou|
|SF|[435](/dev/peps/pep-0435)|Adding an Enum type to the Python standard library|Warsaw, Bendersky, Furman|
|SF|[441](/dev/peps/pep-0441)|Improving Python ZIP Application Support|Holth, Moore|
|SF|[442](/dev/peps/pep-0442)|Safe object finalization|Pitrou|
|SF|[443](/dev/peps/pep-0443)|Single-dispatch generic functions|Langa|
|SF|[445](/dev/peps/pep-0445)|Add new APIs to customize Python memory allocators|Stinner|
|SF|[446](/dev/peps/pep-0446)|Make newly created file descriptors non-inheritable|Stinner|
|SF|[448](/dev/peps/pep-0448)|Additional Unpacking Generalizations|Landau|
|SF|[450](/dev/peps/pep-0450)|Adding A Statistics Module To The Standard Library|D'Aprano|
|SF|[451](/dev/peps/pep-0451)|A ModuleSpec Type for the Import System|Snow|
|SF|[453](/dev/peps/pep-0453)|Explicit bootstrapping of pip in Python installations|Stufft, Coghlan|
|SF|[454](/dev/peps/pep-0454)|Add a new tracemalloc module to trace Python memory ...|Stinner|
|SF|[456](/dev/peps/pep-0456)|Secure and interchangeable hash algorithm|Heimes|
|SF|[461](/dev/peps/pep-0461)|Adding % formatting to bytes and bytearray|Furman|
|SF|[465](/dev/peps/pep-0465)|A dedicated infix operator for matrix multiplication|Smith|
|SF|[466](/dev/peps/pep-0466)|Network Security Enhancements for Python 2.7.x|Coghlan|
|SF|[468](/dev/peps/pep-0468)|Preserving the order of **kwargs in a function.|Snow|
|SF|[471](/dev/peps/pep-0471)|os.scandir() function -- a better and faster ...|Hoyt|
|SF|[475](/dev/peps/pep-0475)|Retry system calls failing with EINTR|Natali, Stinner|
|SF|[476](/dev/peps/pep-0476)|Enabling certificate verification by default for ...|Gaynor|
|SF|[477](/dev/peps/pep-0477)|Backport ensurepip ([PEP 453](/dev/peps/pep-0453)) to Python 2.7|Stufft, Coghlan|
|SF|[479](/dev/peps/pep-0479)|Change StopIteration handling inside generators|Angelico, GvR|
|SF|[485](/dev/peps/pep-0485)|A Function for testing approximate equality|Barker|
|SF|[486](/dev/peps/pep-0486)|Make the Python Launcher aware of virtual environments|Moore|
|SF|[487](/dev/peps/pep-0487)|Simpler customisation of class creation|Teichmann|
|SF|[488](/dev/peps/pep-0488)|Elimination of PYO files|Cannon|
|SF|[489](/dev/peps/pep-0489)|Multi-phase extension module initialization|Viktorin, Behnel, Coghlan|
|SF|[492](/dev/peps/pep-0492)|Coroutines with async and await syntax|Selivanov|
|SF|[493](/dev/peps/pep-0493)|HTTPS verification migration tools for Python 2.7|Coghlan, Kuska, Lemburg|
|SF|[495](/dev/peps/pep-0495)|Local Time Disambiguation|Belopolsky, Peters|
|SF|[498](/dev/peps/pep-0498)|Literal String Interpolation|Smith|
|SF|[506](/dev/peps/pep-0506)|Adding A Secrets Module To The Standard Library|D'Aprano|
|SF|[509](/dev/peps/pep-0509)|Add a private version to dict|Stinner|
|SF|[515](/dev/peps/pep-0515)|Underscores in Numeric Literals|Brandl, Storchaka|
|SF|[519](/dev/peps/pep-0519)|Adding a file system path protocol|Cannon, Zevenhoven|
|SF|[520](/dev/peps/pep-0520)|Preserving Class Attribute Definition Order|Snow|
|SF|[523](/dev/peps/pep-0523)|Adding a frame evaluation API to CPython|Cannon, Viehland|
|SF|[524](/dev/peps/pep-0524)|Make os.urandom() blocking on Linux|Stinner|
|SF|[525](/dev/peps/pep-0525)|Asynchronous Generators|Selivanov|
|SF|[526](/dev/peps/pep-0526)|Syntax for Variable Annotations|Gonzalez, House, Levkivskyi, Roach, GvR|
|SF|[528](/dev/peps/pep-0528)|Change Windows console encoding to UTF-8|Dower|
|SF|[529](/dev/peps/pep-0529)|Change Windows filesystem encoding to UTF-8|Dower|
|SF|[530](/dev/peps/pep-0530)|Asynchronous Comprehensions|Selivanov|
|SF|[538](/dev/peps/pep-0538)|Coercing the legacy C locale to a UTF-8 based locale|Coghlan|
|SF|[539](/dev/peps/pep-0539)|A New C-API for Thread-Local Storage in CPython|Bray, Yamamoto|
|SF|[540](/dev/peps/pep-0540)|Add a new UTF-8 Mode|Stinner|
|SF|[552](/dev/peps/pep-0552)|Deterministic pycs|Peterson|
|SF|[553](/dev/peps/pep-0553)|Built-in breakpoint()|Warsaw|
|SF|[562](/dev/peps/pep-0562)|Module \_\_getattr\_\_ and \_\_dir\_\_|Levkivskyi|
|SF|[564](/dev/peps/pep-0564)|Add new time functions with nanosecond resolution|Stinner|
|SF|[565](/dev/peps/pep-0565)|Show DeprecationWarning in \_\_main\_\_|Coghlan|
|SF|[566](/dev/peps/pep-0566)|Metadata for Python Software Packages 2.1|Ingram|
|SF|[567](/dev/peps/pep-0567)|Context Variables|Selivanov|
|SF|[628](/dev/peps/pep-0628)|Add math.tau|Coghlan|
|SF|[3101](/dev/peps/pep-3101)|Advanced String Formatting|Talin|
|SF|[3102](/dev/peps/pep-3102)|Keyword-Only Arguments|Talin|
|SF|[3104](/dev/peps/pep-3104)|Access to Names in Outer Scopes|Yee|
|SF|[3105](/dev/peps/pep-3105)|Make print a function|Brandl|
|SF|[3106](/dev/peps/pep-3106)|Revamping dict.keys(), .values() and .items()|GvR|
|SF|[3107](/dev/peps/pep-3107)|Function Annotations|Winter, Lownds|
|SF|[3108](/dev/peps/pep-3108)|Standard Library Reorganization|Cannon|
|SF|[3109](/dev/peps/pep-3109)|Raising Exceptions in Python 3000|Winter|
|SF|[3110](/dev/peps/pep-3110)|Catching Exceptions in Python 3000|Winter|
|SF|[3111](/dev/peps/pep-3111)|Simple input built-in in Python 3000|Roberge|
|SF|[3112](/dev/peps/pep-3112)|Bytes literals in Python 3000|Orendorff|
|SF|[3113](/dev/peps/pep-3113)|Removal of Tuple Parameter Unpacking|Cannon|
|SF|[3114](/dev/peps/pep-3114)|Renaming iterator.next() to iterator.\_\_next\_\_()|Yee|
|SF|[3115](/dev/peps/pep-3115)|Metaclasses in Python 3000|Talin|
|SF|[3116](/dev/peps/pep-3116)|New I/O|Stutzbach, GvR, Verdone|
|SF|[3118](/dev/peps/pep-3118)|Revising the buffer protocol|Oliphant, Banks|
|SF|[3119](/dev/peps/pep-3119)|Introducing Abstract Base Classes|GvR, Talin|
|SF|[3120](/dev/peps/pep-3120)|Using UTF-8 as the default source encoding|von Löwis|
|SF|[3123](/dev/peps/pep-3123)|Making PyObject_HEAD conform to standard C|von Löwis|
|SF|[3127](/dev/peps/pep-3127)|Integer Literal Support and Syntax|Maupin|
|SF|[3129](/dev/peps/pep-3129)|Class Decorators|Winter|
|SF|[3131](/dev/peps/pep-3131)|Supporting Non-ASCII Identifiers|von Löwis|
|SF|[3132](/dev/peps/pep-3132)|Extended Iterable Unpacking|Brandl|
|SF|[3134](/dev/peps/pep-3134)|Exception Chaining and Embedded Tracebacks|Yee|
|SF|[3135](/dev/peps/pep-3135)|New Super|Spealman, Delaney, Ryan|
|SF|[3137](/dev/peps/pep-3137)|Immutable Bytes and Mutable Buffer|GvR|
|SF|[3138](/dev/peps/pep-3138)|String representation in Python 3000|Ishimoto|
|SF|[3141](/dev/peps/pep-3141)|A Type Hierarchy for Numbers|Yasskin|
|SF|[3144](/dev/peps/pep-3144)|IP Address Manipulation Library for the Python ...|Moody|
|SF|[3147](/dev/peps/pep-3147)|PYC Repository Directories|Warsaw|
|SF|[3148](/dev/peps/pep-3148)|futures - execute computations asynchronously|Quinlan|
|SF|[3149](/dev/peps/pep-3149)|ABI version tagged .so files|Warsaw|
|SF|[3151](/dev/peps/pep-3151)|Reworking the OS and IO exception hierarchy|Pitrou|
|SF|[3154](/dev/peps/pep-3154)|Pickle protocol version 4|Pitrou|
|SF|[3155](/dev/peps/pep-3155)|Qualified name for classes and functions|Pitrou|
|SF|[3156](/dev/peps/pep-3156)|Asynchronous IO Support Rebooted: the "asyncio" Module|GvR
  
[Historical Meta-PEPs and Informational PEPs](#id12)
----------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|PF|[2](/dev/peps/pep-0002)|Procedure for Adding New Modules|Faassen|
|IF|[160](/dev/peps/pep-0160)|Python 1.6 Release Schedule|Drake|
|IF|[200](/dev/peps/pep-0200)|Python 2.0 Release Schedule|Hylton|
|IF|[226](/dev/peps/pep-0226)|Python 2.1 Release Schedule|Hylton|
|IF|[251](/dev/peps/pep-0251)|Python 2.2 Release Schedule|Warsaw, GvR|
|IF|[283](/dev/peps/pep-0283)|Python 2.3 Release Schedule|GvR|
|IF|[320](/dev/peps/pep-0320)|Python 2.4 Release Schedule|Warsaw, Hettinger, Baxter|
|PF|[347](/dev/peps/pep-0347)|Migrating the Python CVS to Subversion|von Löwis|
|IF|[356](/dev/peps/pep-0356)|Python 2.5 Release Schedule|Norwitz, GvR, Baxter|
|PF|[360](/dev/peps/pep-0360)|Externally Maintained Packages|Cannon|
|IF|[361](/dev/peps/pep-0361)|Python 2.6 and 3.0 Release Schedule|Norwitz, Warsaw|
|PF|[374](/dev/peps/pep-0374)|Choosing a distributed VCS for the Python project|Cannon, Turnbull, Vassalotti, Warsaw, Ochtman|
|IF|[375](/dev/peps/pep-0375)|Python 3.1 Release Schedule|Peterson|
|PF|[385](/dev/peps/pep-0385)|Migrating from Subversion to Mercurial|Ochtman, Pitrou, Brandl|
|IF|[392](/dev/peps/pep-0392)|Python 3.2 Release Schedule|Brandl|
|IF|[398](/dev/peps/pep-0398)|Python 3.3 Release Schedule|Brandl|
|PS|[438](/dev/peps/pep-0438)|Transitioning to release-file hosting on PyPI|Krekel, Meyer|
|PF|[449](/dev/peps/pep-0449)|Removal of the PyPI Mirror Auto Discovery and ...|Stufft|
|PF|[464](/dev/peps/pep-0464)|Removal of the PyPI Mirror Authenticity API|Stufft|
|PF|[470](/dev/peps/pep-0470)|Removing External Hosting Support on PyPI|Stufft|
|PF|[512](/dev/peps/pep-0512)|Migrating from hg.python.org to GitHub|Cannon|
|PA|[527](/dev/peps/pep-0527)|Removing Un(der)used file types/extensions on PyPI|Stufft|
|PF|[541](/dev/peps/pep-0541)|Package Index Name Retention|Langa|
|PF|[545](/dev/peps/pep-0545)|Python Documentation Translations|Palard, Naoki, Stinner|
|PF|[3000](/dev/peps/pep-3000)|Python 3000|GvR|
|PF|[3002](/dev/peps/pep-3002)|Procedure for Backwards-Incompatible Changes|Bethard|
|PF|[3003](/dev/peps/pep-3003)|Python Language Moratorium|Cannon, Noller, GvR|
|PF|[3099](/dev/peps/pep-3099)|Things that will Not Change in Python 3000|Brandl|
|PF|[3100](/dev/peps/pep-3100)|Miscellaneous Python 3.0 Plans|Cannon|
|PA|[8001](/dev/peps/pep-8001)|Python Governance Voting Process|Cannon, Heimes, Stufft, Snow, Smith, Langa, Wijaya, Smith, Salgado, Hettinger, Einat, Peters, Ware
  
[Deferred PEPs (postponed pending further research or updates)](#id13)
----------------------------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|SD|[213](/dev/peps/pep-0213)|Attribute Access Handlers|Prescod|
|SD|[219](/dev/peps/pep-0219)|Stackless Python|McMillan|
|SD|[222](/dev/peps/pep-0222)|Web Library Enhancements|Kuchling|
|SD|[233](/dev/peps/pep-0233)|Python Online Help|Prescod|
|SD|[262](/dev/peps/pep-0262)|A Database of Installed Python Packages|Kuchling|
|SD|[267](/dev/peps/pep-0267)|Optimized Access to Module Namespaces|Hylton|
|SD|[269](/dev/peps/pep-0269)|Pgen Module for Python|Riehl|
|SD|[280](/dev/peps/pep-0280)|Optimizing access to globals|GvR|
|SD|[286](/dev/peps/pep-0286)|Enhanced Argument Tuples|von Löwis|
|SD|[312](/dev/peps/pep-0312)|Simple Implicit Lambda|Suzi, Martelli|
|SD|[316](/dev/peps/pep-0316)|Programming by Contract for Python|Way|
|SD|[323](/dev/peps/pep-0323)|Copyable Iterators|Martelli|
|SD|[337](/dev/peps/pep-0337)|Logging Usage in the Standard Library|Dubner|
|SD|[349](/dev/peps/pep-0349)|Allow str() to return unicode strings|Schemenauer|
|SD|[368](/dev/peps/pep-0368)|Standard image protocol and class|Mastrodomenico|
|ID|[396](/dev/peps/pep-0396)|Module Version Numbers|Warsaw|
|SD|[400](/dev/peps/pep-0400)|Deprecate codecs.StreamReader and codecs.StreamWriter|Stinner|
|SD|[403](/dev/peps/pep-0403)|General purpose decorator clause (aka "@in" clause)|Coghlan|
|PD|[407](/dev/peps/pep-0407)|New release cycle and introducing long-term support ...|Pitrou, Brandl, Warsaw|
|SD|[419](/dev/peps/pep-0419)|Protecting cleanup statements from interruptions|Colomiets|
|ID|[423](/dev/peps/pep-0423)|Naming conventions and recipes related to packaging|Bryon|
|ID|[444](/dev/peps/pep-0444)|Python Web3 Interface|McDonough, Ronacher|
|SD|[501](/dev/peps/pep-0501)|General purpose string interpolation|Coghlan|
|SD|[505](/dev/peps/pep-0505)|None-aware operators|Haase, Dower|
|SD|[532](/dev/peps/pep-0532)|A circuit breaking protocol and binary operators|Coghlan, Haase|
|SD|[535](/dev/peps/pep-0535)|Rich comparison chaining|Coghlan|
|SD|[547](/dev/peps/pep-0547)|Running extension modules using the -m option|Plch, Viktorin|
|SD|[568](/dev/peps/pep-0568)|Generator-sensitivity for Context Variables|Smith|
|SD|[3124](/dev/peps/pep-3124)|Overloading, Generic Functions, Interfaces, and ...|Eby|
|SD|[3143](/dev/peps/pep-3143)|Standard daemon process library|Finney|
|SD|[3150](/dev/peps/pep-3150)|Statement local namespaces (aka "given" clause)|Coghlan
  
[Abandoned, Withdrawn, and Rejected PEPs](#id14)
------------------------------------------------
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|PW|[3](/dev/peps/pep-0003)|Guidelines for Handling Bug Reports|Hylton|
|PW|[9](/dev/peps/pep-0009)|Sample Plaintext PEP Template|Warsaw|
|PR|[42](/dev/peps/pep-0042)|Feature Requests|Hylton|
|IS|[102](/dev/peps/pep-0102)|Doing Python Micro Releases|Baxter, Warsaw, GvR|
|IW|[103](/dev/peps/pep-0103)|Collecting information about git|Broytman|
|SR|[204](/dev/peps/pep-0204)|Range Literals|Wouters|
|IW|[206](/dev/peps/pep-0206)|Python Advanced Library|Kuchling|
|SW|[209](/dev/peps/pep-0209)|Multi-dimensional Arrays|Barrett, Oliphant|
|SR|[210](/dev/peps/pep-0210)|Decoupling the Interpreter Loop|Ascher|
|SR|[211](/dev/peps/pep-0211)|Adding A New Outer Product Operator|Wilson|
|SR|[212](/dev/peps/pep-0212)|Loop Counter Iteration|Schneider-Kamp|
|SS|[215](/dev/peps/pep-0215)|String Interpolation|Yee|
|IR|[216](/dev/peps/pep-0216)|Docstring Format|Zadka|
|IR|[220](/dev/peps/pep-0220)|Coroutines, Generators, Continuations|McMillan|
|SR|[224](/dev/peps/pep-0224)|Attribute Docstrings|Lemburg|
|SR|[225](/dev/peps/pep-0225)|Elementwise/Objectwise Operators|Zhu, Lielens|
|SW|[228](/dev/peps/pep-0228)|Reworking Python's Numeric Model|Zadka, GvR|
|SR|[231](/dev/peps/pep-0231)|\_\_findattr\_\_()|Warsaw|
|SR|[239](/dev/peps/pep-0239)|Adding a Rational Type to Python|Craig, Zadka|
|SR|[240](/dev/peps/pep-0240)|Adding a Rational Literal to Python|Craig, Zadka|
|SR|[242](/dev/peps/pep-0242)|Numeric Kinds|Dubois|
|SW|[243](/dev/peps/pep-0243)|Module Repository Upload Mechanism|Reifschneider|
|SR|[244](/dev/peps/pep-0244)|The directive statement|von Löwis|
|SR|[245](/dev/peps/pep-0245)|Python Interface Syntax|Pelletier|
|SR|[246](/dev/peps/pep-0246)|Object Adaptation|Martelli, Evans|
|SR|[254](/dev/peps/pep-0254)|Making Classes Look More Like Types|GvR|
|SR|[256](/dev/peps/pep-0256)|Docstring Processing System Framework|Goodger|
|SR|[258](/dev/peps/pep-0258)|Docutils Design Specification|Goodger|
|SR|[259](/dev/peps/pep-0259)|Omit printing newline after newline|GvR|
|SR|[265](/dev/peps/pep-0265)|Sorting Dictionaries by Value|Griffin|
|SW|[266](/dev/peps/pep-0266)|Optimizing Global Variable/Attribute Access|Montanaro|
|SR|[268](/dev/peps/pep-0268)|Extended HTTP functionality and WebDAV|Stein|
|SR|[270](/dev/peps/pep-0270)|uniq method for list objects|Petrone|
|SR|[271](/dev/peps/pep-0271)|Prefixing sys.path by command line option|Giacometti|
|SR|[275](/dev/peps/pep-0275)|Switching on Multiple Values|Lemburg|
|SR|[276](/dev/peps/pep-0276)|Simple Iterator for ints|Althoff|
|SR|[281](/dev/peps/pep-0281)|Loop Counter Iteration with range and xrange|Hetland|
|SR|[284](/dev/peps/pep-0284)|Integer for-loops|Eppstein, Ewing|
|SW|[288](/dev/peps/pep-0288)|Generators Attributes and Exceptions|Hettinger|
|SR|[294](/dev/peps/pep-0294)|Type Names in the types Module|Tirosh|
|SR|[295](/dev/peps/pep-0295)|Interpretation of multiline string constants|Koltsov|
|SW|[296](/dev/peps/pep-0296)|Adding a bytes Object Type|Gilbert|
|SR|[297](/dev/peps/pep-0297)|Support for System Upgrades|Lemburg|
|SW|[298](/dev/peps/pep-0298)|The Locked Buffer Interface|Heller|
|SR|[299](/dev/peps/pep-0299)|Special \_\_main\_\_() function in modules|Epler|
|SR|[303](/dev/peps/pep-0303)|Extend divmod() for Multiple Divisors|Bellman|
|SW|[304](/dev/peps/pep-0304)|Controlling Generation of Bytecode Files|Montanaro|
|IW|[306](/dev/peps/pep-0306)|How to Change Python's Grammar|Hudson, Diederich, Coghlan, Peterson|
|SR|[310](/dev/peps/pep-0310)|Reliable Acquisition/Release Pairs|Hudson, Moore|
|SR|[313](/dev/peps/pep-0313)|Adding Roman Numeral Literals to Python|Meyer|
|SR|[315](/dev/peps/pep-0315)|Enhanced While Loop|Hettinger, Carroll|
|SR|[317](/dev/peps/pep-0317)|Eliminate Implicit Exception Instantiation|Taschuk|
|SR|[319](/dev/peps/pep-0319)|Python Synchronize/Asynchronize Block|Pelletier|
|SW|[321](/dev/peps/pep-0321)|Date/Time Parsing and Formatting|Kuchling|
|SR|[325](/dev/peps/pep-0325)|Resource-Release Support for Generators|Pedroni|
|SR|[326](/dev/peps/pep-0326)|A Case for Top and Bottom Values|Carlson, Reedy|
|SR|[329](/dev/peps/pep-0329)|Treating Builtins as Constants in the Standard Library|Hettinger|
|SR|[330](/dev/peps/pep-0330)|Python Bytecode Verification|Pelletier|
|SR|[332](/dev/peps/pep-0332)|Byte vectors and String/Unicode Unification|Montanaro|
|SW|[334](/dev/peps/pep-0334)|Simple Coroutines via SuspendIteration|Evans|
|SR|[335](/dev/peps/pep-0335)|Overloadable Boolean Operators|Ewing|
|SR|[336](/dev/peps/pep-0336)|Make None Callable|McClelland|
|IW|[339](/dev/peps/pep-0339)|Design of the CPython Compiler|Cannon|
|SR|[340](/dev/peps/pep-0340)|Anonymous Block Statements|GvR|
|SS|[344](/dev/peps/pep-0344)|Exception Chaining and Embedded Tracebacks|Yee|
|SW|[346](/dev/peps/pep-0346)|User Defined ("with") Statements|Coghlan|
|SR|[348](/dev/peps/pep-0348)|Exception Reorganization for Python 3.0|Cannon|
|IR|[350](/dev/peps/pep-0350)|Codetags|Elliott|
|SR|[351](/dev/peps/pep-0351)|The freeze protocol|Warsaw|
|SS|[354](/dev/peps/pep-0354)|Enumerations in Python|Finney|
|SR|[355](/dev/peps/pep-0355)|Path - Object oriented filesystem paths|Lindqvist|
|SW|[359](/dev/peps/pep-0359)|The "make" Statement|Bethard|
|SR|[363](/dev/peps/pep-0363)|Syntax For Dynamic Attribute Access|North|
|SW|[364](/dev/peps/pep-0364)|Transitioning to the Py3K Standard Library|Warsaw|
|SR|[365](/dev/peps/pep-0365)|Adding the pkg_resources module|Eby|
|SS|[367](/dev/peps/pep-0367)|New Super|Spealman, Delaney|
|SW|[369](/dev/peps/pep-0369)|Post import hooks|Heimes|
|SR|[377](/dev/peps/pep-0377)|Allow \_\_enter\_\_() methods to skip the statement body|Coghlan|
|SW|[379](/dev/peps/pep-0379)|Adding an Assignment Expression|Whitley|
|SR|[382](/dev/peps/pep-0382)|Namespace Packages|v. Löwis|
|SS|[386](/dev/peps/pep-0386)|Changing the version comparison module in Distutils|Ziadé|
|SR|[390](/dev/peps/pep-0390)|Static metadata for Distutils|Ziadé|
|SW|[395](/dev/peps/pep-0395)|Qualified Names for Modules|Coghlan|
|PR|[401](/dev/peps/pep-0401)|BDFL Retirement|Warsaw, Cannon|
|SR|[402](/dev/peps/pep-0402)|Simplified Package Layout and Partitioning|Eby|
|SW|[406](/dev/peps/pep-0406)|Improved Encapsulation of Import State|Coghlan, Slodkowicz|
|SR|[408](/dev/peps/pep-0408)|Standard library \_\_preview\_\_ package|Coghlan, Bendersky|
|SR|[410](/dev/peps/pep-0410)|Use decimal.Decimal type for timestamps|Stinner|
|PW|[413](/dev/peps/pep-0413)|Faster evolution of the Python Standard Library|Coghlan|
|SR|[416](/dev/peps/pep-0416)|Add a frozendict builtin type|Stinner|
|SW|[422](/dev/peps/pep-0422)|Simpler customisation of class creation|Coghlan, Urban|
|IW|[426](/dev/peps/pep-0426)|Metadata for Python Software Packages 2.0|Coghlan, Holth, Stufft|
|SW|[431](/dev/peps/pep-0431)|Time zone support improvements|Regebro|
|SS|[433](/dev/peps/pep-0433)|Easier suppression of file descriptor inheritance|Stinner|
|SR|[437](/dev/peps/pep-0437)|A DSL for specifying signatures, annotations and ...|Krah|
|SR|[439](/dev/peps/pep-0439)|Inclusion of implicit pip bootstrap in Python ...|Jones|
|SR|[455](/dev/peps/pep-0455)|Adding a key-transforming dictionary to collections|Pitrou|
|SW|[459](/dev/peps/pep-0459)|Standard Metadata Extensions for Python Software ...|Coghlan|
|SW|[460](/dev/peps/pep-0460)|Add binary interpolation and formatting|Pitrou|
|PW|[462](/dev/peps/pep-0462)|Core development workflow automation for CPython|Coghlan|
|SR|[463](/dev/peps/pep-0463)|Exception-catching expressions|Angelico|
|SW|[469](/dev/peps/pep-0469)|Migration of dict iteration code to Python 3|Coghlan|
|PW|[474](/dev/peps/pep-0474)|Creating forge.python.org|Coghlan|
|PW|[481](/dev/peps/pep-0481)|Migrate CPython to Git, Github, and Phabricator|Stufft|
|SR|[490](/dev/peps/pep-0490)|Chain exceptions at C level|Stinner|
|IR|[496](/dev/peps/pep-0496)|Environment Markers|Polley|
|SR|[500](/dev/peps/pep-0500)|A protocol for delegating datetime methods to their ...|Belopolsky, Peters|
|SW|[504](/dev/peps/pep-0504)|Using the System RNG by default|Coghlan|
|PR|[507](/dev/peps/pep-0507)|Migrate CPython to Git and GitLab|Warsaw|
|SR|[510](/dev/peps/pep-0510)|Specialize functions with guards|Stinner|
|SR|[511](/dev/peps/pep-0511)|API for code transformers|Stinner|
|SR|[516](/dev/peps/pep-0516)|Build system abstraction for pip/conda etc|Collins, Smith|
|SW|[521](/dev/peps/pep-0521)|Managing global context via 'with' blocks in ...|Smith|
|SR|[522](/dev/peps/pep-0522)|Allow BlockingIOError in security sensitive APIs|Coghlan, Smith|
|SW|[531](/dev/peps/pep-0531)|Existence checking operators|Coghlan|
|SR|[546](/dev/peps/pep-0546)|Backport ssl.MemoryBIO and ssl.SSLObject to Python 2.7|Stinner, Benfield|
|SR|[548](/dev/peps/pep-0548)|More Flexible Loop Control|Murray|
|SR|[549](/dev/peps/pep-0549)|Instance Descriptors|Hastings|
|SW|[550](/dev/peps/pep-0550)|Execution Context|Selivanov, Pranskevichus|
|SW|[555](/dev/peps/pep-0555)|Context-local variables (contextvars)|Zevenhoven|
|SR|[559](/dev/peps/pep-0559)|Built-in noop()|Warsaw|
|SW|[575](/dev/peps/pep-0575)|Unifying function/method classes|Demeyer|
|SW|[577](/dev/peps/pep-0577)|Augmented Assignment Expressions|Coghlan|
|IW|[583](/dev/peps/pep-0583)|A Concurrency Memory Model for Python|Yasskin|
|SR|[666](/dev/peps/pep-0666)|Reject Foolish Indentation|Creighton|
|SR|[754](/dev/peps/pep-0754)|IEEE 754 Floating Point Special Values|Warnes|
|PW|[3001](/dev/peps/pep-3001)|Procedure for reviewing and improving standard ...|Brandl|
|SR|[3103](/dev/peps/pep-3103)|A Switch/Case Statement|GvR|
|SR|[3117](/dev/peps/pep-3117)|Postfix type declarations|Brandl|
|SR|[3122](/dev/peps/pep-3122)|Delineation of the main module|Cannon|
|SR|[3125](/dev/peps/pep-3125)|Remove Backslash Continuation|Jewett|
|SR|[3126](/dev/peps/pep-3126)|Remove Implicit String Concatenation|Jewett, Hettinger|
|SR|[3128](/dev/peps/pep-3128)|BList: A Faster List-like Type|Stutzbach|
|SR|[3130](/dev/peps/pep-3130)|Access to Current Module/Class/Function|Jewett|
|SR|[3133](/dev/peps/pep-3133)|Introducing Roles|Winter|
|SR|[3136](/dev/peps/pep-3136)|Labeled break and continue|Chisholm|
|SR|[3139](/dev/peps/pep-3139)|Cleaning out sys and the "interpreter" module|Peterson|
|SR|[3140](/dev/peps/pep-3140)|str(container) should call str(item), not repr(item)|Broytman, Jewett|
|SR|[3142](/dev/peps/pep-3142)|Add a "while" clause to generator expressions|Britton|
|SW|[3145](/dev/peps/pep-3145)|Asynchronous I/O For subprocess.Popen|Pruitt, McCreary, Carlson|
|SW|[3146](/dev/peps/pep-3146)|Merging Unladen Swallow into CPython|Winter, Yasskin, Kleckner|
|SR|[3152](/dev/peps/pep-3152)|Cofunctions|Ewing|
|SS|[3153](/dev/peps/pep-3153)|Asynchronous IO support|Houtven|
|IR|[8010](/dev/peps/pep-8010)|The Technical Leader Governance Model|Warsaw|
|IR|[8011](/dev/peps/pep-8011)|Python Governance Model Lead by Trio of Pythonistas|Wijaya, Warsaw|
|IR|[8012](/dev/peps/pep-8012)|The Community Governance Model|Langa|
|IR|[8013](/dev/peps/pep-8013)|The External Council Governance Model|Dower|
|IR|[8014](/dev/peps/pep-8014)|The Commons Governance Model|Jansen|
|IR|[8015](/dev/peps/pep-8015)|Organization of the Python community|Stinner
  
[Numerical Index](#id15)
========================
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|P|[1](/dev/peps/pep-0001)|PEP Purpose and Guidelines|Warsaw, Hylton, Goodger, Coghlan|
|PF|[2](/dev/peps/pep-0002)|Procedure for Adding New Modules|Faassen|
|PW|[3](/dev/peps/pep-0003)|Guidelines for Handling Bug Reports|Hylton|
|P|[4](/dev/peps/pep-0004)|Deprecation of Standard Modules|Cannon, von Löwis|
|P|[5](/dev/peps/pep-0005)|Guidelines for Language Evolution|Prescod|
|P|[6](/dev/peps/pep-0006)|Bug Fix Releases|Aahz, Baxter|
|P|[7](/dev/peps/pep-0007)|Style Guide for C Code|GvR, Warsaw|
|P|[8](/dev/peps/pep-0008)|Style Guide for Python Code|GvR, Warsaw, Coghlan|
|PW|[9](/dev/peps/pep-0009)|Sample Plaintext PEP Template|Warsaw|
|P|[10](/dev/peps/pep-0010)|Voting Guidelines|Warsaw|
|P|[11](/dev/peps/pep-0011)|Removing support for little used platforms|von Löwis, Cannon|
|P|[12](/dev/peps/pep-0012)|Sample reStructuredText PEP Template|Goodger, Warsaw|
|I|[13](/dev/peps/pep-0013)|Python Language Governance|and community|
|I|[20](/dev/peps/pep-0020)|The Zen of Python|Peters|
|PR|[42](/dev/peps/pep-0042)|Feature Requests|Hylton|
|SF|[100](/dev/peps/pep-0100)|Python Unicode Integration|Lemburg|
|I|[101](/dev/peps/pep-0101)|Doing Python Releases 101|Warsaw, GvR|
|IS|[102](/dev/peps/pep-0102)|Doing Python Micro Releases|Baxter, Warsaw, GvR|
|IW|[103](/dev/peps/pep-0103)|Collecting information about git|Broytman|
|IF|[160](/dev/peps/pep-0160)|Python 1.6 Release Schedule|Drake|
|IF|[200](/dev/peps/pep-0200)|Python 2.0 Release Schedule|Hylton|
|SF|[201](/dev/peps/pep-0201)|Lockstep Iteration|Warsaw|
|SF|[202](/dev/peps/pep-0202)|List Comprehensions|Warsaw|
|SF|[203](/dev/peps/pep-0203)|Augmented Assignments|Wouters|
|SR|[204](/dev/peps/pep-0204)|Range Literals|Wouters|
|SF|[205](/dev/peps/pep-0205)|Weak References|Drake|
|IW|[206](/dev/peps/pep-0206)|Python Advanced Library|Kuchling|
|SF|[207](/dev/peps/pep-0207)|Rich Comparisons|GvR, Ascher|
|SF|[208](/dev/peps/pep-0208)|Reworking the Coercion Model|Schemenauer, Lemburg|
|SW|[209](/dev/peps/pep-0209)|Multi-dimensional Arrays|Barrett, Oliphant|
|SR|[210](/dev/peps/pep-0210)|Decoupling the Interpreter Loop|Ascher|
|SR|[211](/dev/peps/pep-0211)|Adding A New Outer Product Operator|Wilson|
|SR|[212](/dev/peps/pep-0212)|Loop Counter Iteration|Schneider-Kamp|
|SD|[213](/dev/peps/pep-0213)|Attribute Access Handlers|Prescod|
|SF|[214](/dev/peps/pep-0214)|Extended Print Statement|Warsaw|
|SS|[215](/dev/peps/pep-0215)|String Interpolation|Yee|
|IR|[216](/dev/peps/pep-0216)|Docstring Format|Zadka|
|SF|[217](/dev/peps/pep-0217)|Display Hook for Interactive Use|Zadka|
|SF|[218](/dev/peps/pep-0218)|Adding a Built-In Set Object Type|Wilson, Hettinger|
|SD|[219](/dev/peps/pep-0219)|Stackless Python|McMillan|
|IR|[220](/dev/peps/pep-0220)|Coroutines, Generators, Continuations|McMillan|
|SF|[221](/dev/peps/pep-0221)|Import As|Wouters|
|SD|[222](/dev/peps/pep-0222)|Web Library Enhancements|Kuchling|
|SF|[223](/dev/peps/pep-0223)|Change the Meaning of \x Escapes|Peters|
|SR|[224](/dev/peps/pep-0224)|Attribute Docstrings|Lemburg|
|SR|[225](/dev/peps/pep-0225)|Elementwise/Objectwise Operators|Zhu, Lielens|
|IF|[226](/dev/peps/pep-0226)|Python 2.1 Release Schedule|Hylton|
|SF|[227](/dev/peps/pep-0227)|Statically Nested Scopes|Hylton|
|SW|[228](/dev/peps/pep-0228)|Reworking Python's Numeric Model|Zadka, GvR|
|SF|[229](/dev/peps/pep-0229)|Using Distutils to Build Python|Kuchling|
|SF|[230](/dev/peps/pep-0230)|Warning Framework|GvR|
|SR|[231](/dev/peps/pep-0231)|\_\_findattr\_\_()|Warsaw|
|SF|[232](/dev/peps/pep-0232)|Function Attributes|Warsaw|
|SD|[233](/dev/peps/pep-0233)|Python Online Help|Prescod|
|SF|[234](/dev/peps/pep-0234)|Iterators|Yee, GvR|
|SF|[235](/dev/peps/pep-0235)|Import on Case-Insensitive Platforms|Peters|
|SF|[236](/dev/peps/pep-0236)|Back to the \_\_future\_\_|Peters|
|SF|[237](/dev/peps/pep-0237)|Unifying Long Integers and Integers|Zadka, GvR|
|SF|[238](/dev/peps/pep-0238)|Changing the Division Operator|Zadka, GvR|
|SR|[239](/dev/peps/pep-0239)|Adding a Rational Type to Python|Craig, Zadka|
|SR|[240](/dev/peps/pep-0240)|Adding a Rational Literal to Python|Craig, Zadka|
|SF|[241](/dev/peps/pep-0241)|Metadata for Python Software Packages|Kuchling|
|SR|[242](/dev/peps/pep-0242)|Numeric Kinds|Dubois|
|SW|[243](/dev/peps/pep-0243)|Module Repository Upload Mechanism|Reifschneider|
|SR|[244](/dev/peps/pep-0244)|The directive statement|von Löwis|
|SR|[245](/dev/peps/pep-0245)|Python Interface Syntax|Pelletier|
|SR|[246](/dev/peps/pep-0246)|Object Adaptation|Martelli, Evans|
|IF|[247](/dev/peps/pep-0247)|API for Cryptographic Hash Functions|Kuchling|
|IF|[248](/dev/peps/pep-0248)|Python Database API Specification v1.0|Lemburg|
|IF|[249](/dev/peps/pep-0249)|Python Database API Specification v2.0|Lemburg|
|SF|[250](/dev/peps/pep-0250)|Using site-packages on Windows|Moore|
|IF|[251](/dev/peps/pep-0251)|Python 2.2 Release Schedule|Warsaw, GvR|
|SF|[252](/dev/peps/pep-0252)|Making Types Look More Like Classes|GvR|
|SF|[253](/dev/peps/pep-0253)|Subtyping Built-in Types|GvR|
|SR|[254](/dev/peps/pep-0254)|Making Classes Look More Like Types|GvR|
|SF|[255](/dev/peps/pep-0255)|Simple Generators|Schemenauer, Peters, Hetland|
|SR|[256](/dev/peps/pep-0256)|Docstring Processing System Framework|Goodger|
|I|[257](/dev/peps/pep-0257)|Docstring Conventions|Goodger, GvR|
|SR|[258](/dev/peps/pep-0258)|Docutils Design Specification|Goodger|
|SR|[259](/dev/peps/pep-0259)|Omit printing newline after newline|GvR|
|SF|[260](/dev/peps/pep-0260)|Simplify xrange()|GvR|
|SF|[261](/dev/peps/pep-0261)|Support for "wide" Unicode characters|Prescod|
|SD|[262](/dev/peps/pep-0262)|A Database of Installed Python Packages|Kuchling|
|SF|[263](/dev/peps/pep-0263)|Defining Python Source Code Encodings|Lemburg, von Löwis|
|SF|[264](/dev/peps/pep-0264)|Future statements in simulated shells|Hudson|
|SR|[265](/dev/peps/pep-0265)|Sorting Dictionaries by Value|Griffin|
|SW|[266](/dev/peps/pep-0266)|Optimizing Global Variable/Attribute Access|Montanaro|
|SD|[267](/dev/peps/pep-0267)|Optimized Access to Module Namespaces|Hylton|
|SR|[268](/dev/peps/pep-0268)|Extended HTTP functionality and WebDAV|Stein|
|SD|[269](/dev/peps/pep-0269)|Pgen Module for Python|Riehl|
|SR|[270](/dev/peps/pep-0270)|uniq method for list objects|Petrone|
|SR|[271](/dev/peps/pep-0271)|Prefixing sys.path by command line option|Giacometti|
|IF|[272](/dev/peps/pep-0272)|API for Block Encryption Algorithms v1.0|Kuchling|
|SF|[273](/dev/peps/pep-0273)|Import Modules from Zip Archives|Ahlstrom|
|SF|[274](/dev/peps/pep-0274)|Dict Comprehensions|Warsaw|
|SR|[275](/dev/peps/pep-0275)|Switching on Multiple Values|Lemburg|
|SR|[276](/dev/peps/pep-0276)|Simple Iterator for ints|Althoff|
|SF|[277](/dev/peps/pep-0277)|Unicode file name support for Windows NT|Hodgson|
|SF|[278](/dev/peps/pep-0278)|Universal Newline Support|Jansen|
|SF|[279](/dev/peps/pep-0279)|The enumerate() built-in function|Hettinger|
|SD|[280](/dev/peps/pep-0280)|Optimizing access to globals|GvR|
|SR|[281](/dev/peps/pep-0281)|Loop Counter Iteration with range and xrange|Hetland|
|SF|[282](/dev/peps/pep-0282)|A Logging System|Sajip, Mick|
|IF|[283](/dev/peps/pep-0283)|Python 2.3 Release Schedule|GvR|
|SR|[284](/dev/peps/pep-0284)|Integer for-loops|Eppstein, Ewing|
|SF|[285](/dev/peps/pep-0285)|Adding a bool type|GvR|
|SD|[286](/dev/peps/pep-0286)|Enhanced Argument Tuples|von Löwis|
|I|[287](/dev/peps/pep-0287)|reStructuredText Docstring Format|Goodger|
|SW|[288](/dev/peps/pep-0288)|Generators Attributes and Exceptions|Hettinger|
|SF|[289](/dev/peps/pep-0289)|Generator Expressions|Hettinger|
|I|[290](/dev/peps/pep-0290)|Code Migration and Modernization|Hettinger|
|IF|[291](/dev/peps/pep-0291)|Backward Compatibility for the Python 2 Standard ...|Norwitz|
|SF|[292](/dev/peps/pep-0292)|Simpler String Substitutions|Warsaw|
|SF|[293](/dev/peps/pep-0293)|Codec Error Handling Callbacks|Dörwald|
|SR|[294](/dev/peps/pep-0294)|Type Names in the types Module|Tirosh|
|SR|[295](/dev/peps/pep-0295)|Interpretation of multiline string constants|Koltsov|
|SW|[296](/dev/peps/pep-0296)|Adding a bytes Object Type|Gilbert|
|SR|[297](/dev/peps/pep-0297)|Support for System Upgrades|Lemburg|
|SW|[298](/dev/peps/pep-0298)|The Locked Buffer Interface|Heller|
|SR|[299](/dev/peps/pep-0299)|Special \_\_main\_\_() function in modules|Epler|
|SF|[301](/dev/peps/pep-0301)|Package Index and Metadata for Distutils|Jones|
|SF|[302](/dev/peps/pep-0302)|New Import Hooks|JvR, Moore|
|SR|[303](/dev/peps/pep-0303)|Extend divmod() for Multiple Divisors|Bellman|
|SW|[304](/dev/peps/pep-0304)|Controlling Generation of Bytecode Files|Montanaro|
|SF|[305](/dev/peps/pep-0305)|CSV File API|Altis, Cole, McNamara, Montanaro, Wells|
|IW|[306](/dev/peps/pep-0306)|How to Change Python's Grammar|Hudson, Diederich, Coghlan, Peterson|
|SF|[307](/dev/peps/pep-0307)|Extensions to the pickle protocol|GvR, Peters|
|SF|[308](/dev/peps/pep-0308)|Conditional Expressions|GvR, Hettinger|
|SF|[309](/dev/peps/pep-0309)|Partial Function Application|Harris|
|SR|[310](/dev/peps/pep-0310)|Reliable Acquisition/Release Pairs|Hudson, Moore|
|SF|[311](/dev/peps/pep-0311)|Simplified Global Interpreter Lock Acquisition for ...|Hammond|
|SD|[312](/dev/peps/pep-0312)|Simple Implicit Lambda|Suzi, Martelli|
|SR|[313](/dev/peps/pep-0313)|Adding Roman Numeral Literals to Python|Meyer|
|SF|[314](/dev/peps/pep-0314)|Metadata for Python Software Packages v1.1|Kuchling, Jones|
|SR|[315](/dev/peps/pep-0315)|Enhanced While Loop|Hettinger, Carroll|
|SD|[316](/dev/peps/pep-0316)|Programming by Contract for Python|Way|
|SR|[317](/dev/peps/pep-0317)|Eliminate Implicit Exception Instantiation|Taschuk|
|SF|[318](/dev/peps/pep-0318)|Decorators for Functions and Methods|Smith|
|SR|[319](/dev/peps/pep-0319)|Python Synchronize/Asynchronize Block|Pelletier|
|IF|[320](/dev/peps/pep-0320)|Python 2.4 Release Schedule|Warsaw, Hettinger, Baxter|
|SW|[321](/dev/peps/pep-0321)|Date/Time Parsing and Formatting|Kuchling|
|SF|[322](/dev/peps/pep-0322)|Reverse Iteration|Hettinger|
|SD|[323](/dev/peps/pep-0323)|Copyable Iterators|Martelli|
|SF|[324](/dev/peps/pep-0324)|subprocess - New process module|Astrand|
|SR|[325](/dev/peps/pep-0325)|Resource-Release Support for Generators|Pedroni|
|SR|[326](/dev/peps/pep-0326)|A Case for Top and Bottom Values|Carlson, Reedy|
|SF|[327](/dev/peps/pep-0327)|Decimal Data Type|Batista|
|SF|[328](/dev/peps/pep-0328)|Imports: Multi-Line and Absolute/Relative|Aahz|
|SR|[329](/dev/peps/pep-0329)|Treating Builtins as Constants in the Standard Library|Hettinger|
|SR|[330](/dev/peps/pep-0330)|Python Bytecode Verification|Pelletier|
|SF|[331](/dev/peps/pep-0331)|Locale-Independent Float/String Conversions|Reis|
|SR|[332](/dev/peps/pep-0332)|Byte vectors and String/Unicode Unification|Montanaro|
|IF|[333](/dev/peps/pep-0333)|Python Web Server Gateway Interface v1.0|Eby|
|SW|[334](/dev/peps/pep-0334)|Simple Coroutines via SuspendIteration|Evans|
|SR|[335](/dev/peps/pep-0335)|Overloadable Boolean Operators|Ewing|
|SR|[336](/dev/peps/pep-0336)|Make None Callable|McClelland|
|SD|[337](/dev/peps/pep-0337)|Logging Usage in the Standard Library|Dubner|
|SF|[338](/dev/peps/pep-0338)|Executing modules as scripts|Coghlan|
|IW|[339](/dev/peps/pep-0339)|Design of the CPython Compiler|Cannon|
|SR|[340](/dev/peps/pep-0340)|Anonymous Block Statements|GvR|
|SF|[341](/dev/peps/pep-0341)|Unifying try-except and try-finally|Brandl|
|SF|[342](/dev/peps/pep-0342)|Coroutines via Enhanced Generators|GvR, Eby|
|SF|[343](/dev/peps/pep-0343)|The "with" Statement|GvR, Coghlan|
|SS|[344](/dev/peps/pep-0344)|Exception Chaining and Embedded Tracebacks|Yee|
|SF|[345](/dev/peps/pep-0345)|Metadata for Python Software Packages 1.2|Jones|
|SW|[346](/dev/peps/pep-0346)|User Defined ("with") Statements|Coghlan|
|PF|[347](/dev/peps/pep-0347)|Migrating the Python CVS to Subversion|von Löwis|
|SR|[348](/dev/peps/pep-0348)|Exception Reorganization for Python 3.0|Cannon|
|SD|[349](/dev/peps/pep-0349)|Allow str() to return unicode strings|Schemenauer|
|IR|[350](/dev/peps/pep-0350)|Codetags|Elliott|
|SR|[351](/dev/peps/pep-0351)|The freeze protocol|Warsaw|
|SF|[352](/dev/peps/pep-0352)|Required Superclass for Exceptions|Cannon, GvR|
|SF|[353](/dev/peps/pep-0353)|Using ssize_t as the index type|von Löwis|
|SS|[354](/dev/peps/pep-0354)|Enumerations in Python|Finney|
|SR|[355](/dev/peps/pep-0355)|Path - Object oriented filesystem paths|Lindqvist|
|IF|[356](/dev/peps/pep-0356)|Python 2.5 Release Schedule|Norwitz, GvR, Baxter|
|SF|[357](/dev/peps/pep-0357)|Allowing Any Object to be Used for Slicing|Oliphant|
|SF|[358](/dev/peps/pep-0358)|The "bytes" Object|Schemenauer, GvR|
|SW|[359](/dev/peps/pep-0359)|The "make" Statement|Bethard|
|PF|[360](/dev/peps/pep-0360)|Externally Maintained Packages|Cannon|
|IF|[361](/dev/peps/pep-0361)|Python 2.6 and 3.0 Release Schedule|Norwitz, Warsaw|
|SF|[362](/dev/peps/pep-0362)|Function Signature Object|Cannon, Seo, Selivanov, Hastings|
|SR|[363](/dev/peps/pep-0363)|Syntax For Dynamic Attribute Access|North|
|SW|[364](/dev/peps/pep-0364)|Transitioning to the Py3K Standard Library|Warsaw|
|SR|[365](/dev/peps/pep-0365)|Adding the pkg_resources module|Eby|
|SF|[366](/dev/peps/pep-0366)|Main module explicit relative imports|Coghlan|
|SS|[367](/dev/peps/pep-0367)|New Super|Spealman, Delaney|
|SD|[368](/dev/peps/pep-0368)|Standard image protocol and class|Mastrodomenico|
|SW|[369](/dev/peps/pep-0369)|Post import hooks|Heimes|
|SF|[370](/dev/peps/pep-0370)|Per user site-packages directory|Heimes|
|SF|[371](/dev/peps/pep-0371)|Addition of the multiprocessing package to the ...|Noller, Oudkerk|
|SF|[372](/dev/peps/pep-0372)|Adding an ordered dictionary to collections|Ronacher, Hettinger|
|I|[373](/dev/peps/pep-0373)|Python 2.7 Release Schedule|Peterson|
|PF|[374](/dev/peps/pep-0374)|Choosing a distributed VCS for the Python project|Cannon, Turnbull, Vassalotti, Warsaw, Ochtman|
|IF|[375](/dev/peps/pep-0375)|Python 3.1 Release Schedule|Peterson|
|SF|[376](/dev/peps/pep-0376)|Database of Installed Python Distributions|Ziadé|
|SR|[377](/dev/peps/pep-0377)|Allow \_\_enter\_\_() methods to skip the statement body|Coghlan|
|SF|[378](/dev/peps/pep-0378)|Format Specifier for Thousands Separator|Hettinger|
|SW|[379](/dev/peps/pep-0379)|Adding an Assignment Expression|Whitley|
|SF|[380](/dev/peps/pep-0380)|Syntax for Delegating to a Subgenerator|Ewing|
|S|[381](/dev/peps/pep-0381)|Mirroring infrastructure for PyPI|Ziadé, v. Löwis|
|SR|[382](/dev/peps/pep-0382)|Namespace Packages|v. Löwis|
|SF|[383](/dev/peps/pep-0383)|Non-decodable Bytes in System Character Interfaces|v. Löwis|
|SF|[384](/dev/peps/pep-0384)|Defining a Stable ABI|v. Löwis|
|PF|[385](/dev/peps/pep-0385)|Migrating from Subversion to Mercurial|Ochtman, Pitrou, Brandl|
|SS|[386](/dev/peps/pep-0386)|Changing the version comparison module in Distutils|Ziadé|
|P|[387](/dev/peps/pep-0387)|Backwards Compatibility Policy|Peterson|
|SF|[389](/dev/peps/pep-0389)|argparse - New Command Line Parsing Module|Bethard|
|SR|[390](/dev/peps/pep-0390)|Static metadata for Distutils|Ziadé|
|SF|[391](/dev/peps/pep-0391)|Dictionary-Based Configuration For Logging|Sajip|
|IF|[392](/dev/peps/pep-0392)|Python 3.2 Release Schedule|Brandl|
|SF|[393](/dev/peps/pep-0393)|Flexible String Representation|v. Löwis|
|I|[394](/dev/peps/pep-0394)|The "python" Command on Unix-Like Systems|Staley, Coghlan, Warsaw, Viktorin|
|SW|[395](/dev/peps/pep-0395)|Qualified Names for Modules|Coghlan|
|ID|[396](/dev/peps/pep-0396)|Module Version Numbers|Warsaw|
|SF|[397](/dev/peps/pep-0397)|Python launcher for Windows|Hammond, v. Löwis|
|IF|[398](/dev/peps/pep-0398)|Python 3.3 Release Schedule|Brandl|
|IF|[399](/dev/peps/pep-0399)|Pure Python/C Accelerator Module Compatibility ...|Cannon|
|SD|[400](/dev/peps/pep-0400)|Deprecate codecs.StreamReader and codecs.StreamWriter|Stinner|
|PR|[401](/dev/peps/pep-0401)|BDFL Retirement|Warsaw, Cannon|
|SR|[402](/dev/peps/pep-0402)|Simplified Package Layout and Partitioning|Eby|
|SD|[403](/dev/peps/pep-0403)|General purpose decorator clause (aka "@in" clause)|Coghlan|
|IF|[404](/dev/peps/pep-0404)|Python 2.8 Un-release Schedule|Warsaw|
|SF|[405](/dev/peps/pep-0405)|Python Virtual Environments|Meyer|
|SW|[406](/dev/peps/pep-0406)|Improved Encapsulation of Import State|Coghlan, Slodkowicz|
|PD|[407](/dev/peps/pep-0407)|New release cycle and introducing long-term support ...|Pitrou, Brandl, Warsaw|
|SR|[408](/dev/peps/pep-0408)|Standard library \_\_preview\_\_ package|Coghlan, Bendersky|
|SF|[409](/dev/peps/pep-0409)|Suppressing exception context|Furman|
|SR|[410](/dev/peps/pep-0410)|Use decimal.Decimal type for timestamps|Stinner|
|I|[411](/dev/peps/pep-0411)|Provisional packages in the Python standard library|Coghlan, Bendersky|
|SF|[412](/dev/peps/pep-0412)|Key-Sharing Dictionary|Shannon|
|PW|[413](/dev/peps/pep-0413)|Faster evolution of the Python Standard Library|Coghlan|
|SF|[414](/dev/peps/pep-0414)|Explicit Unicode Literal for Python 3.3|Ronacher, Coghlan|
|SF|[415](/dev/peps/pep-0415)|Implement context suppression with exception attributes|Peterson|
|SR|[416](/dev/peps/pep-0416)|Add a frozendict builtin type|Stinner|
|SF|[417](/dev/peps/pep-0417)|Including mock in the Standard Library|Foord|
|SF|[418](/dev/peps/pep-0418)|Add monotonic time, performance counter, and ...|Simpson, Jewett, Turnbull, Stinner|
|SD|[419](/dev/peps/pep-0419)|Protecting cleanup statements from interruptions|Colomiets|
|SF|[420](/dev/peps/pep-0420)|Implicit Namespace Packages|Smith|
|SF|[421](/dev/peps/pep-0421)|Adding sys.implementation|Snow|
|SW|[422](/dev/peps/pep-0422)|Simpler customisation of class creation|Coghlan, Urban|
|ID|[423](/dev/peps/pep-0423)|Naming conventions and recipes related to packaging|Bryon|
|SF|[424](/dev/peps/pep-0424)|A method for exposing a length hint|Gaynor|
|SF|[425](/dev/peps/pep-0425)|Compatibility Tags for Built Distributions|Holth|
|IW|[426](/dev/peps/pep-0426)|Metadata for Python Software Packages 2.0|Coghlan, Holth, Stufft|
|SF|[427](/dev/peps/pep-0427)|The Wheel Binary Package Format 1.0|Holth|
|SF|[428](/dev/peps/pep-0428)|The pathlib module -- object-oriented filesystem paths|Pitrou|
|I|[429](/dev/peps/pep-0429)|Python 3.4 Release Schedule|Hastings|
|IF|[430](/dev/peps/pep-0430)|Migrating to Python 3 as the default online ...|Coghlan|
|SW|[431](/dev/peps/pep-0431)|Time zone support improvements|Regebro|
|S|[432](/dev/peps/pep-0432)|Restructuring the CPython startup sequence|Coghlan|
|SS|[433](/dev/peps/pep-0433)|Easier suppression of file descriptor inheritance|Stinner|
|I|[434](/dev/peps/pep-0434)|IDLE Enhancement Exception for All Branches|Rovito, Reedy|
|SF|[435](/dev/peps/pep-0435)|Adding an Enum type to the Python standard library|Warsaw, Bendersky, Furman|
|S|[436](/dev/peps/pep-0436)|The Argument Clinic DSL|Hastings|
|SR|[437](/dev/peps/pep-0437)|A DSL for specifying signatures, annotations and ...|Krah|
|PS|[438](/dev/peps/pep-0438)|Transitioning to release-file hosting on PyPI|Krekel, Meyer|
|SR|[439](/dev/peps/pep-0439)|Inclusion of implicit pip bootstrap in Python ...|Jones|
|I|[440](/dev/peps/pep-0440)|Version Identification and Dependency Specification|Coghlan, Stufft|
|SF|[441](/dev/peps/pep-0441)|Improving Python ZIP Application Support|Holth, Moore|
|SF|[442](/dev/peps/pep-0442)|Safe object finalization|Pitrou|
|SF|[443](/dev/peps/pep-0443)|Single-dispatch generic functions|Langa|
|ID|[444](/dev/peps/pep-0444)|Python Web3 Interface|McDonough, Ronacher|
|SF|[445](/dev/peps/pep-0445)|Add new APIs to customize Python memory allocators|Stinner|
|SF|[446](/dev/peps/pep-0446)|Make newly created file descriptors non-inheritable|Stinner|
|S|[447](/dev/peps/pep-0447)|Add \_\_getdescriptor\_\_ method to metaclass|Oussoren|
|SF|[448](/dev/peps/pep-0448)|Additional Unpacking Generalizations|Landau|
|PF|[449](/dev/peps/pep-0449)|Removal of the PyPI Mirror Auto Discovery and ...|Stufft|
|SF|[450](/dev/peps/pep-0450)|Adding A Statistics Module To The Standard Library|D'Aprano|
|SF|[451](/dev/peps/pep-0451)|A ModuleSpec Type for the Import System|Snow|
|I|[452](/dev/peps/pep-0452)|API for Cryptographic Hash Functions v2.0|Kuchling, Heimes|
|SF|[453](/dev/peps/pep-0453)|Explicit bootstrapping of pip in Python installations|Stufft, Coghlan|
|SF|[454](/dev/peps/pep-0454)|Add a new tracemalloc module to trace Python memory ...|Stinner|
|SR|[455](/dev/peps/pep-0455)|Adding a key-transforming dictionary to collections|Pitrou|
|SF|[456](/dev/peps/pep-0456)|Secure and interchangeable hash algorithm|Heimes|
|I|[457](/dev/peps/pep-0457)|Syntax For Positional-Only Parameters|Hastings|
|S|[458](/dev/peps/pep-0458)|Surviving a Compromise of PyPI|Kuppusamy, Diaz, Stufft, Cappos|
|SW|[459](/dev/peps/pep-0459)|Standard Metadata Extensions for Python Software ...|Coghlan|
|SW|[460](/dev/peps/pep-0460)|Add binary interpolation and formatting|Pitrou|
|SF|[461](/dev/peps/pep-0461)|Adding % formatting to bytes and bytearray|Furman|
|PW|[462](/dev/peps/pep-0462)|Core development workflow automation for CPython|Coghlan|
|SR|[463](/dev/peps/pep-0463)|Exception-catching expressions|Angelico|
|PF|[464](/dev/peps/pep-0464)|Removal of the PyPI Mirror Authenticity API|Stufft|
|SF|[465](/dev/peps/pep-0465)|A dedicated infix operator for matrix multiplication|Smith|
|SF|[466](/dev/peps/pep-0466)|Network Security Enhancements for Python 2.7.x|Coghlan|
|S|[467](/dev/peps/pep-0467)|Minor API improvements for binary sequences|Coghlan, Furman|
|SF|[468](/dev/peps/pep-0468)|Preserving the order of **kwargs in a function.|Snow|
|SW|[469](/dev/peps/pep-0469)|Migration of dict iteration code to Python 3|Coghlan|
|PF|[470](/dev/peps/pep-0470)|Removing External Hosting Support on PyPI|Stufft|
|SF|[471](/dev/peps/pep-0471)|os.scandir() function -- a better and faster ...|Hoyt|
|S|[472](/dev/peps/pep-0472)|Support for indexing with keyword arguments|Borini, Martinot-Lagarde|
|S|[473](/dev/peps/pep-0473)|Adding structured data to built-in exceptions|Kreft|
|PW|[474](/dev/peps/pep-0474)|Creating forge.python.org|Coghlan|
|SF|[475](/dev/peps/pep-0475)|Retry system calls failing with EINTR|Natali, Stinner|
|SF|[476](/dev/peps/pep-0476)|Enabling certificate verification by default for ...|Gaynor|
|SF|[477](/dev/peps/pep-0477)|Backport ensurepip ([PEP 453](/dev/peps/pep-0453)) to Python 2.7|Stufft, Coghlan|
|I|[478](/dev/peps/pep-0478)|Python 3.5 Release Schedule|Hastings|
|SF|[479](/dev/peps/pep-0479)|Change StopIteration handling inside generators|Angelico, GvR|
|S|[480](/dev/peps/pep-0480)|Surviving a Compromise of PyPI: The Maximum ...|Kuppusamy, Diaz, Stufft, Cappos|
|PW|[481](/dev/peps/pep-0481)|Migrate CPython to Git, Github, and Phabricator|Stufft|
|I|[482](/dev/peps/pep-0482)|Literature Overview for Type Hints|Langa|
|I|[483](/dev/peps/pep-0483)|The Theory of Type Hints|GvR, Levkivskyi|
|SP|[484](/dev/peps/pep-0484)|Type Hints|GvR, Lehtosalo, Langa|
|SF|[485](/dev/peps/pep-0485)|A Function for testing approximate equality|Barker|
|SF|[486](/dev/peps/pep-0486)|Make the Python Launcher aware of virtual environments|Moore|
|SF|[487](/dev/peps/pep-0487)|Simpler customisation of class creation|Teichmann|
|SF|[488](/dev/peps/pep-0488)|Elimination of PYO files|Cannon|
|SF|[489](/dev/peps/pep-0489)|Multi-phase extension module initialization|Viktorin, Behnel, Coghlan|
|SR|[490](/dev/peps/pep-0490)|Chain exceptions at C level|Stinner|
|S|[491](/dev/peps/pep-0491)|The Wheel Binary Package Format 1.9|Holth|
|SF|[492](/dev/peps/pep-0492)|Coroutines with async and await syntax|Selivanov|
|SF|[493](/dev/peps/pep-0493)|HTTPS verification migration tools for Python 2.7|Coghlan, Kuska, Lemburg|
|I|[494](/dev/peps/pep-0494)|Python 3.6 Release Schedule|Deily|
|SF|[495](/dev/peps/pep-0495)|Local Time Disambiguation|Belopolsky, Peters|
|IR|[496](/dev/peps/pep-0496)|Environment Markers|Polley|
|P|[497](/dev/peps/pep-0497)|A standard mechanism for backward compatibility|Schofield|
|SF|[498](/dev/peps/pep-0498)|Literal String Interpolation|Smith|
|S|[499](/dev/peps/pep-0499)|python -m foo should bind ...|Simpson|
|SR|[500](/dev/peps/pep-0500)|A protocol for delegating datetime methods to their ...|Belopolsky, Peters|
|SD|[501](/dev/peps/pep-0501)|General purpose string interpolation|Coghlan|
|I|[502](/dev/peps/pep-0502)|String Interpolation - Extended Discussion|Miller|
|IA|[503](/dev/peps/pep-0503)|Simple Repository API|Stufft|
|SW|[504](/dev/peps/pep-0504)|Using the System RNG by default|Coghlan|
|SD|[505](/dev/peps/pep-0505)|None-aware operators|Haase, Dower|
|SF|[506](/dev/peps/pep-0506)|Adding A Secrets Module To The Standard Library|D'Aprano|
|PR|[507](/dev/peps/pep-0507)|Migrate CPython to Git and GitLab|Warsaw|
|I|[508](/dev/peps/pep-0508)|Dependency specification for Python Software Packages|Collins|
|SF|[509](/dev/peps/pep-0509)|Add a private version to dict|Stinner|
|SR|[510](/dev/peps/pep-0510)|Specialize functions with guards|Stinner|
|SR|[511](/dev/peps/pep-0511)|API for code transformers|Stinner|
|PF|[512](/dev/peps/pep-0512)|Migrating from hg.python.org to GitHub|Cannon|
|I|[513](/dev/peps/pep-0513)|A Platform Tag for Portable Linux Built Distributions|McGibbon, Smith|
|I|[514](/dev/peps/pep-0514)|Python registration in the Windows registry|Dower|
|SF|[515](/dev/peps/pep-0515)|Underscores in Numeric Literals|Brandl, Storchaka|
|SR|[516](/dev/peps/pep-0516)|Build system abstraction for pip/conda etc|Collins, Smith|
|SP|[517](/dev/peps/pep-0517)|A build-system independent format for source trees|Smith, Kluyver|
|SP|[518](/dev/peps/pep-0518)|Specifying Minimum Build System Requirements for ...|Cannon, Smith, Stufft|
|SF|[519](/dev/peps/pep-0519)|Adding a file system path protocol|Cannon, Zevenhoven|
|SF|[520](/dev/peps/pep-0520)|Preserving Class Attribute Definition Order|Snow|
|SW|[521](/dev/peps/pep-0521)|Managing global context via 'with' blocks in ...|Smith|
|SR|[522](/dev/peps/pep-0522)|Allow BlockingIOError in security sensitive APIs|Coghlan, Smith|
|SF|[523](/dev/peps/pep-0523)|Adding a frame evaluation API to CPython|Cannon, Viehland|
|SF|[524](/dev/peps/pep-0524)|Make os.urandom() blocking on Linux|Stinner|
|SF|[525](/dev/peps/pep-0525)|Asynchronous Generators|Selivanov|
|SF|[526](/dev/peps/pep-0526)|Syntax for Variable Annotations|Gonzalez, House, Levkivskyi, Roach, GvR|
|PA|[527](/dev/peps/pep-0527)|Removing Un(der)used file types/extensions on PyPI|Stufft|
|SF|[528](/dev/peps/pep-0528)|Change Windows console encoding to UTF-8|Dower|
|SF|[529](/dev/peps/pep-0529)|Change Windows filesystem encoding to UTF-8|Dower|
|SF|[530](/dev/peps/pep-0530)|Asynchronous Comprehensions|Selivanov|
|SW|[531](/dev/peps/pep-0531)|Existence checking operators|Coghlan|
|SD|[532](/dev/peps/pep-0532)|A circuit breaking protocol and binary operators|Coghlan, Haase|
|S|[533](/dev/peps/pep-0533)|Deterministic cleanup for iterators|Smith|
|S|[534](/dev/peps/pep-0534)|Distributing a Subset of the Standard Library|Orsava, Viktorin, Coghlan|
|SD|[535](/dev/peps/pep-0535)|Rich comparison chaining|Coghlan|
|S|[536](/dev/peps/pep-0536)|Final Grammar for Literal String Interpolation|Angerer|
|I|[537](/dev/peps/pep-0537)|Python 3.7 Release Schedule|Deily|
|SF|[538](/dev/peps/pep-0538)|Coercing the legacy C locale to a UTF-8 based locale|Coghlan|
|SF|[539](/dev/peps/pep-0539)|A New C-API for Thread-Local Storage in CPython|Bray, Yamamoto|
|SF|[540](/dev/peps/pep-0540)|Add a new UTF-8 Mode|Stinner|
|PF|[541](/dev/peps/pep-0541)|Package Index Name Retention|Langa|
|S|[542](/dev/peps/pep-0542)|Dot Notation Assignment In Function Header|Meskanen|
|S|[543](/dev/peps/pep-0543)|A Unified TLS API for Python|Benfield, Heimes|
|S|[544](/dev/peps/pep-0544)|Protocols: Structural subtyping (static duck typing)|Levkivskyi, Lehtosalo, Langa|
|PF|[545](/dev/peps/pep-0545)|Python Documentation Translations|Palard, Naoki, Stinner|
|SR|[546](/dev/peps/pep-0546)|Backport ssl.MemoryBIO and ssl.SSLObject to Python 2.7|Stinner, Benfield|
|SD|[547](/dev/peps/pep-0547)|Running extension modules using the -m option|Plch, Viktorin|
|SR|[548](/dev/peps/pep-0548)|More Flexible Loop Control|Murray|
|SR|[549](/dev/peps/pep-0549)|Instance Descriptors|Hastings|
|SW|[550](/dev/peps/pep-0550)|Execution Context|Selivanov, Pranskevichus|
|I|[551](/dev/peps/pep-0551)|Security transparency in the Python runtime|Dower|
|SF|[552](/dev/peps/pep-0552)|Deterministic pycs|Peterson|
|SF|[553](/dev/peps/pep-0553)|Built-in breakpoint()|Warsaw|
|S|[554](/dev/peps/pep-0554)|Multiple Interpreters in the Stdlib|Snow|
|SW|[555](/dev/peps/pep-0555)|Context-local variables (contextvars)|Zevenhoven|
|S|[556](/dev/peps/pep-0556)|Threaded garbage collection|Pitrou|
|SA|[557](/dev/peps/pep-0557)|Data Classes|Smith|
|S|[558](/dev/peps/pep-0558)|Defined semantics for locals()|Coghlan|
|SR|[559](/dev/peps/pep-0559)|Built-in noop()|Warsaw|
|SA|[560](/dev/peps/pep-0560)|Core support for typing module and generic types|Levkivskyi|
|SA|[561](/dev/peps/pep-0561)|Distributing and Packaging Type Information|Smith|
|SF|[562](/dev/peps/pep-0562)|Module \_\_getattr\_\_ and \_\_dir\_\_|Levkivskyi|
|SA|[563](/dev/peps/pep-0563)|Postponed Evaluation of Annotations|Langa|
|SF|[564](/dev/peps/pep-0564)|Add new time functions with nanosecond resolution|Stinner|
|SF|[565](/dev/peps/pep-0565)|Show DeprecationWarning in \_\_main\_\_|Coghlan|
|SF|[566](/dev/peps/pep-0566)|Metadata for Python Software Packages 2.1|Ingram|
|SF|[567](/dev/peps/pep-0567)|Context Variables|Selivanov|
|SD|[568](/dev/peps/pep-0568)|Generator-sensitivity for Context Variables|Smith|
|I|[569](/dev/peps/pep-0569)|Python 3.8 Release Schedule|Langa|
|S|[570](/dev/peps/pep-0570)|Python Positional-Only Parameters|Hastings, Galindo, Corchero|
|I|[571](/dev/peps/pep-0571)|The manylinux2010 Platform Tag|Williams, Thomas, Kluyver|
|SA|[572](/dev/peps/pep-0572)|Assignment Expressions|Angelico, Peters, GvR|
|P|[573](/dev/peps/pep-0573)|Module State Access from C Extension Methods|Viktorin, Coghlan, Snow, Plch|
|S|[574](/dev/peps/pep-0574)|Pickle protocol 5 with out-of-band data|Pitrou|
|SW|[575](/dev/peps/pep-0575)|Unifying function/method classes|Demeyer|
|S|[576](/dev/peps/pep-0576)|Rationalize Built-in function classes|Shannon|
|SW|[577](/dev/peps/pep-0577)|Augmented Assignment Expressions|Coghlan|
|S|[578](/dev/peps/pep-0578)|Python Runtime Audit Hooks|Dower|
|I|[579](/dev/peps/pep-0579)|Refactoring C functions and methods|Demeyer|
|S|[580](/dev/peps/pep-0580)|The C call protocol|Demeyer|
|P|[581](/dev/peps/pep-0581)|Using GitHub Issues for CPython|Wijaya|
|S|[582](/dev/peps/pep-0582)|Python local packages directory|Das, Dower, Stufft, Coghlan|
|IW|[583](/dev/peps/pep-0583)|A Concurrency Memory Model for Python|Yasskin|
|SF|[628](/dev/peps/pep-0628)|Add math.tau|Coghlan|
|SR|[666](/dev/peps/pep-0666)|Reject Foolish Indentation|Creighton|
|SR|[754](/dev/peps/pep-0754)|IEEE 754 Floating Point Special Values|Warnes|
|I|[801](/dev/peps/pep-0801)|Reserved|Warsaw|
|PF|[3000](/dev/peps/pep-3000)|Python 3000|GvR|
|PW|[3001](/dev/peps/pep-3001)|Procedure for reviewing and improving standard ...|Brandl|
|PF|[3002](/dev/peps/pep-3002)|Procedure for Backwards-Incompatible Changes|Bethard|
|PF|[3003](/dev/peps/pep-3003)|Python Language Moratorium|Cannon, Noller, GvR|
|PF|[3099](/dev/peps/pep-3099)|Things that will Not Change in Python 3000|Brandl|
|PF|[3100](/dev/peps/pep-3100)|Miscellaneous Python 3.0 Plans|Cannon|
|SF|[3101](/dev/peps/pep-3101)|Advanced String Formatting|Talin|
|SF|[3102](/dev/peps/pep-3102)|Keyword-Only Arguments|Talin|
|SR|[3103](/dev/peps/pep-3103)|A Switch/Case Statement|GvR|
|SF|[3104](/dev/peps/pep-3104)|Access to Names in Outer Scopes|Yee|
|SF|[3105](/dev/peps/pep-3105)|Make print a function|Brandl|
|SF|[3106](/dev/peps/pep-3106)|Revamping dict.keys(), .values() and .items()|GvR|
|SF|[3107](/dev/peps/pep-3107)|Function Annotations|Winter, Lownds|
|SF|[3108](/dev/peps/pep-3108)|Standard Library Reorganization|Cannon|
|SF|[3109](/dev/peps/pep-3109)|Raising Exceptions in Python 3000|Winter|
|SF|[3110](/dev/peps/pep-3110)|Catching Exceptions in Python 3000|Winter|
|SF|[3111](/dev/peps/pep-3111)|Simple input built-in in Python 3000|Roberge|
|SF|[3112](/dev/peps/pep-3112)|Bytes literals in Python 3000|Orendorff|
|SF|[3113](/dev/peps/pep-3113)|Removal of Tuple Parameter Unpacking|Cannon|
|SF|[3114](/dev/peps/pep-3114)|Renaming iterator.next() to iterator.\_\_next\_\_()|Yee|
|SF|[3115](/dev/peps/pep-3115)|Metaclasses in Python 3000|Talin|
|SF|[3116](/dev/peps/pep-3116)|New I/O|Stutzbach, GvR, Verdone|
|SR|[3117](/dev/peps/pep-3117)|Postfix type declarations|Brandl|
|SF|[3118](/dev/peps/pep-3118)|Revising the buffer protocol|Oliphant, Banks|
|SF|[3119](/dev/peps/pep-3119)|Introducing Abstract Base Classes|GvR, Talin|
|SF|[3120](/dev/peps/pep-3120)|Using UTF-8 as the default source encoding|von Löwis|
|SA|[3121](/dev/peps/pep-3121)|Extension Module Initialization and Finalization|von Löwis|
|SR|[3122](/dev/peps/pep-3122)|Delineation of the main module|Cannon|
|SF|[3123](/dev/peps/pep-3123)|Making PyObject_HEAD conform to standard C|von Löwis|
|SD|[3124](/dev/peps/pep-3124)|Overloading, Generic Functions, Interfaces, and ...|Eby|
|SR|[3125](/dev/peps/pep-3125)|Remove Backslash Continuation|Jewett|
|SR|[3126](/dev/peps/pep-3126)|Remove Implicit String Concatenation|Jewett, Hettinger|
|SF|[3127](/dev/peps/pep-3127)|Integer Literal Support and Syntax|Maupin|
|SR|[3128](/dev/peps/pep-3128)|BList: A Faster List-like Type|Stutzbach|
|SF|[3129](/dev/peps/pep-3129)|Class Decorators|Winter|
|SR|[3130](/dev/peps/pep-3130)|Access to Current Module/Class/Function|Jewett|
|SF|[3131](/dev/peps/pep-3131)|Supporting Non-ASCII Identifiers|von Löwis|
|SF|[3132](/dev/peps/pep-3132)|Extended Iterable Unpacking|Brandl|
|SR|[3133](/dev/peps/pep-3133)|Introducing Roles|Winter|
|SF|[3134](/dev/peps/pep-3134)|Exception Chaining and Embedded Tracebacks|Yee|
|SF|[3135](/dev/peps/pep-3135)|New Super|Spealman, Delaney, Ryan|
|SR|[3136](/dev/peps/pep-3136)|Labeled break and continue|Chisholm|
|SF|[3137](/dev/peps/pep-3137)|Immutable Bytes and Mutable Buffer|GvR|
|SF|[3138](/dev/peps/pep-3138)|String representation in Python 3000|Ishimoto|
|SR|[3139](/dev/peps/pep-3139)|Cleaning out sys and the "interpreter" module|Peterson|
|SR|[3140](/dev/peps/pep-3140)|str(container) should call str(item), not repr(item)|Broytman, Jewett|
|SF|[3141](/dev/peps/pep-3141)|A Type Hierarchy for Numbers|Yasskin|
|SR|[3142](/dev/peps/pep-3142)|Add a "while" clause to generator expressions|Britton|
|SD|[3143](/dev/peps/pep-3143)|Standard daemon process library|Finney|
|SF|[3144](/dev/peps/pep-3144)|IP Address Manipulation Library for the Python ...|Moody|
|SW|[3145](/dev/peps/pep-3145)|Asynchronous I/O For subprocess.Popen|Pruitt, McCreary, Carlson|
|SW|[3146](/dev/peps/pep-3146)|Merging Unladen Swallow into CPython|Winter, Yasskin, Kleckner|
|SF|[3147](/dev/peps/pep-3147)|PYC Repository Directories|Warsaw|
|SF|[3148](/dev/peps/pep-3148)|futures - execute computations asynchronously|Quinlan|
|SF|[3149](/dev/peps/pep-3149)|ABI version tagged .so files|Warsaw|
|SD|[3150](/dev/peps/pep-3150)|Statement local namespaces (aka "given" clause)|Coghlan|
|SF|[3151](/dev/peps/pep-3151)|Reworking the OS and IO exception hierarchy|Pitrou|
|SR|[3152](/dev/peps/pep-3152)|Cofunctions|Ewing|
|SS|[3153](/dev/peps/pep-3153)|Asynchronous IO support|Houtven|
|SF|[3154](/dev/peps/pep-3154)|Pickle protocol version 4|Pitrou|
|SF|[3155](/dev/peps/pep-3155)|Qualified name for classes and functions|Pitrou|
|SF|[3156](/dev/peps/pep-3156)|Asynchronous IO Support Rebooted: the "asyncio" Module|GvR|
|IF|[3333](/dev/peps/pep-3333)|Python Web Server Gateway Interface v1.0.1|Eby|
|I|[8000](/dev/peps/pep-8000)|Python Language Governance Proposal Overview|Warsaw|
|PA|[8001](/dev/peps/pep-8001)|Python Governance Voting Process|Cannon, Heimes, Stufft, Snow, Smith, Langa, Wijaya, Smith, Salgado, Hettinger, Einat, Peters, Ware|
|I|[8002](/dev/peps/pep-8002)|Open Source Governance Survey|Warsaw, Langa, Pitrou, Hellmann, Willing|
|IR|[8010](/dev/peps/pep-8010)|The Technical Leader Governance Model|Warsaw|
|IR|[8011](/dev/peps/pep-8011)|Python Governance Model Lead by Trio of Pythonistas|Wijaya, Warsaw|
|IR|[8012](/dev/peps/pep-8012)|The Community Governance Model|Langa|
|IR|[8013](/dev/peps/pep-8013)|The External Council Governance Model|Dower|
|IR|[8014](/dev/peps/pep-8014)|The Commons Governance Model|Jansen|
|IR|[8015](/dev/peps/pep-8015)|Organization of the Python community|Stinner|
|IA|[8016](/dev/peps/pep-8016)|The Steering Council Model|Smith, Stufft|
|I|[8100](/dev/peps/pep-8100)|January 2019 steering council election|Smith, III
  
[Reserved PEP Numbers](#id16)
=============================
||PEP|PEP Title|PEP Author(s)|
|:----|:----|:----|:----|
|[801](/dev/peps/pep-0801)|RESERVED|Warsaw

[PEP Types Key](#id17)
======================
* > I - Informational PEP
* > P - Process PEP
* > S - Standards Track PEP

[PEP Status Key](#id18)
=======================
* > A - Accepted (Standards Track only) or Active proposal
* > D - Deferred proposal
* > F - Final proposal
* > P - Provisional proposal
* > R - Rejected proposal
* > S - Superseded proposal
* > W - Withdrawn proposal

[References](#id20)
===================
|\[1\]|[PEP 1](/dev/peps/pep-0001): PEP Purpose and Guidelines|
|:----|:----|
|\[2\]|View PEP history online: [https://github.com/python/peps](https://github.com/python/peps)|





