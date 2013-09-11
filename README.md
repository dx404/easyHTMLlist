Easy HTML list Generation Tool

Introduction:
-------------------------------------------------------------------------------
	It is cumbersome to compose error-free nested list in HTML format. It saves
	efforts to have an app to translate indentation-formatted text to html list 
	syntax.  
	 
Sample input:
-------------------------------------------------------------------------------

1 Please Paste or Type your nested list

	1.1 Hello, World!
	1.2 Standard I/O
		1.2.1 Standard Input
			1.2.1.1 ASCII Characters
			1.2.1.2 Unicode
		1.2.2 Standard Output
		1.2.3 Standard Error
2 Try Some Tree Structures 
	2.1 Binary Search Tree
		2.1.1 Red-Black Tree
		2.1.2 AVL Tree
		2.1.3 B-Tree
3 All about non-deterministic 

Sample Output:
-------------------------------------------------------------------------------
Formatted HTML Source Code
<!-- HTML nested list Generation Tool by Duo Zhao -->
<ul class="duo-list">
   <li data-src-line="1" data-level="1">1 Please Paste or Type your nested list
      <ul>
         <li data-src-line="2" data-level="1-1">1.1 Hello, World!</li>
         <li data-src-line="3" data-level="1-2">1.2 Standard I/O
            <ul>
               <li data-src-line="4" data-level="1-2-1">1.2.1 Standard Input
                  <ul>
                     <li data-src-line="5" data-level="1-2-1-1">1.2.1.1 ASCII Characters</li>
                     <li data-src-line="6" data-level="1-2-1-2">1.2.1.2 Unicode</li>
                  </ul>
               </li>
               <li data-src-line="7" data-level="1-2-2">1.2.2 Standard Output</li>
               <li data-src-line="8" data-level="1-2-3">1.2.3 Standard Error</li>
            </ul>
         </li>
      </ul>
   </li>
   <li data-src-line="9" data-level="2">2 Try Some Tree Structures 
      <ul>
         <li data-src-line="10" data-level="2-1">2.1 Binary Search Tree
            <ul>
               <li data-src-line="11" data-level="2-1-1">2.1.1 Red-Black Tree</li>
               <li data-src-line="12" data-level="2-1-2">2.1.2 AVL Tree</li>
               <li data-src-line="13" data-level="2-1-3">2.1.3 B-Tree</li>
            </ul>
         </li>
      </ul>
   </li>
   <li data-src-line="14" data-level="3">3 All about non-deterministic </li>
</ul>
