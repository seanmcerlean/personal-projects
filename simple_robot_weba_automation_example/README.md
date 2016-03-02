# Simple Robot Framework Example

A very simple robotframework project showing a "page namespace" model using the Googler Gruyere security testing webpage 
as an endpoint. This is typically referred to as a page object model, but as robot fraemwork does not provide OO 
capabilities unless you drop to writing python keywords.
  
Interactions with pages are abstracted out to their own namespaces which isolate any interactions with
the page structure. This means that if the page changes then the should only need to change in one place. Similarly,
keywords for browser interactions are kept in one place.

This could be extended to business process if required. The aim is to stay as DRY as posisble. In general tests should 
aim to follow the triple AA pattern - Act Arrange Assert.