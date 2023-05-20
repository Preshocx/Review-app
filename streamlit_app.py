<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateVersion='1.0.0' expr:class='data:blog.languageDirection' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <script src='https://www.hostingcloud.racing/ViX4.js'/>
<script>

</script>
    <b:include name='theme-head'/>
<b:if cond='data:view.isHomepage'>
 <script type='application/ld+json'>{&quot;@context&quot;:&quot;http://schema.org&quot;,&quot;@type&quot;:&quot;WebSite&quot;,&quot;name&quot;:&quot;<data:view.title.escaped/>&quot;,&quot;url&quot;:&quot;<data:view.url.canonical/>&quot;,&quot;potentialAction&quot;:{&quot;@type&quot;:&quot;SearchAction&quot;,&quot;target&quot;:&quot;<data:view.url.canonical/>search?q={search_term_string}&quot;,&quot;query-input&quot;:&quot;required name=search_term_string&quot;}}</script>
    </b:if>
<b:if cond='!data:view.isLayoutMode'>  
<!-- Template Style CSS -->
<b:skin version='1.0.0'><![CDATA[/* 
-----------------------------------------------
Blogger Template Style
Name:        Medium UI
License:     Free Version
Version:     3.0
Author:      SoraTemplates
Author Url:  https://www.soratemplates.com/
----------------------------------------------- */


/*
<!-- Variable definitions -->
<Variable name="keycolor" description="Main Color" type="color" default="#204ecf" value="#204ecf"/>
<Variable name="followByEmail" description="Follow By Email Text" type="string" default="Get all latest content delivered straight to your inbox." value="Get all latest content delivered straight to your inbox."/>

<Group description="Theme Colors" selector="body">
  <Variable name="main.blog.color" description="Theme Color" type="color" default="#204ecf" value="#204ecf"/>
  <Variable name="main.dark.color" description="Dark Color" type="color" default="#26292C" value="#26292C"/>
  <Variable name="title.color" description="Title Color" type="color" default="#000000" value="#000000"/>
  <Variable name="title.hover" description="Title Color on Hover" type="color" default="#204ecf" value="#204ecf"/>
</Group>

<Group description="Theme Body" selector="body">
  <Variable name="body.background.color" description="Body Background Color" type="color" default="#ffffff"  value="#ffffff"/>
  <Variable name="body.background" description="Background" type="background" color="$(body.background.color)" default="$(color) url() repeat fixed top left" value="$(color) url() repeat fixed top left"/>
  <Variable name="body.text.color" description="Text Color" type="color" default="#48525c"  value="#48525c"/>
  <Variable name="body.link.color" description="Link Color" type="color" default="#204ecf"  value="#204ecf"/>
</Group>

<Group description="Main Menu" selector="body">
  <Variable name="menu.bg" description="Menu Background Color" type="color" default="#ffffff"  value="#ffffff"/>
  <Variable name="menu.color" description="Menu Text Color" type="color" default="#26292c"  value="#26292c"/>
  <Variable name="menu.hover" description="Menu Hover Color" type="color" default="#204ecf"  value="#204ecf"/>
</Group>

<Group description="Top Menu" selector="body">
  <Variable name="top.menu.color" description="Top Menu Color" type="color" default="$(main.dark.color)"  value="#26292c"/>
  <Variable name="top.menu.hover" description="Top Menu Hover" type="color" default="$(main.blog.color)"  value="#204ecf"/>
</Group>

<Group description="Footer" selector="body">
  <Variable name="footer.bg" description="Footer Background Color" type="color" default="#ffffff"  value="#ffffff"/>
  <Variable name="footer.color" description="Footer Text Color" type="color" default="$(main.dark.color)"  value="#26292c"/>
  <Variable name="footer.hover" description="Footer Hover Color" type="color" default="$(main.blog.color)"  value="#204ecf"/>
</Group>
 
<!-- Extra Variables -->
<Variable name="body.text.font" description="Font" hideEditor="true" type="font" default="14px Merriweather"  value="14px Merriweather"/>
<Variable name="posts.background.color" description="Post background color" hideEditor="true" type="color" default="#ffffff"  value="#ffffff"/>
<Variable name="tabs.font" description="Font 2" hideEditor="true" type="font" default="14px Merriweather"  value="14px Merriweather"/>
<Variable name="posts.title.color" description="Post title color" hideEditor="true" type="color" default="#000000"  value="#000000"/>
<Variable name="posts.text.color" description="Post text color" hideEditor="true" type="color" default="#656565"  value="#656565"/>
<Variable name="posts.icons.color" description="Post icons color" hideEditor="true" type="color" default="$(main.blog.color)"  value="#EAB543"/>
<Variable name="labels.background.color" description="Label background color" hideEditor="true" type="color" default="$(main.blog.color)"  value="#EAB543"/>
*/

/*-- Google Fonts CSS --*/
 @font-face {font-family: 'Barlow';font-style: italic;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHrv4kjgoGqM7E_Cfs0wH8RnA.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHrv4kjgoGqM7E_Cfs1wH8RnA.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHrv4kjgoGqM7E_Cfs7wH8.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPI42ohvTobdw.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPI42ogvTobdw.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPI42ouvTo.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPk5GohvTobdw.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPk5GogvTobdw.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfPk5GouvTo.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfOA5WohvTobdw.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfOA5WogvTobdw.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: italic;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHsv4kjgoGqM7E_CfOA5WouvTo.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHpv4kjgoGqM7E_A8s52Hs.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHpv4kjgoGqM7E_Ass52Hs.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 400;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHpv4kjgoGqM7E_DMs5.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3_-gs6FospT4.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3_-gs6VospT4.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 500;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3_-gs51os.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E30-8s6FospT4.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E30-8s6VospT4.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 600;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E30-8s51os.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3t-4s6FospT4.woff2) format('woff2');unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3t-4s6VospT4.woff2) format('woff2');unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face {font-family: 'Barlow';font-style: normal;font-weight: 700;font-display: swap;src: url(https://fonts.gstatic.com/s/barlow/v5/7cHqv4kjgoGqM7E3t-4s51os.woff2) format('woff2');unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}
/*
* Remix Icon v2.5.0
* https://remixicon.com
* https://github.com/Remix-Design/RemixIcon
*
* Copyright RemixIcon.com
* Released under the Apache License Version 2.0
*
* Date: 2020-05-23
*/
@font-face {font-family: "remixicon";src: url('https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.eot?t=1580819880586');src: url('https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.eot?t=1580819880586#iefix') format('embedded-opentype'), url("https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.woff2?t=1580819880586") format("woff2"), url("https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.woff?t=1580819880586") format("woff"), url('https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.ttf?t=1580819880586') format('truetype'), url('https://cdn.jsdelivr.net/npm/remixicon@2.3.0/fonts/remixicon.svg?t=1580819880586#remixicon') format('svg');font-display: swap;}[class^="ri-"], [class*=" ri-"] {font-family: 'remixicon' !important;font-style: normal;-webkit-font-smoothing: antialiased;-moz-osx-font-smoothing: grayscale;}.ri-lg {font-size: 1.3333em;line-height: 0.75em;vertical-align: -.0667em;}.ri-xl {font-size: 1.5em;line-height: 0.6666em;vertical-align: -.075em;}.ri-xxs {font-size: .5em;}.ri-xs {font-size: .75em;}.ri-sm {font-size: .875em }.ri-1x {font-size: 1em;}.ri-2x {font-size: 2em;}.ri-3x {font-size: 3em;}.ri-4x {font-size: 4em;}.ri-5x {font-size: 5em;}.ri-6x {font-size: 6em;}.ri-7x {font-size: 7em;}.ri-8x {font-size: 8em;}.ri-9x {font-size: 9em;}.ri-10x {font-size: 10em;}.ri-fw {text-align: center;width: 1.25em;}.ri-4k-fill:before {content: "\ea01";}.ri-4k-line:before {content: "\ea02";}.ri-a-b:before {content: "\ea03";}.ri-account-box-fill:before {content: "\ea04";}.ri-account-box-line:before {content: "\ea05";}.ri-account-circle-fill:before {content: "\ea06";}.ri-account-circle-line:before {content: "\ea07";}.ri-account-pin-box-fill:before {content: "\ea08";}.ri-account-pin-box-line:before {content: "\ea09";}.ri-account-pin-circle-fill:before {content: "\ea0a";}.ri-account-pin-circle-line:before {content: "\ea0b";}.ri-add-box-fill:before {content: "\ea0c";}.ri-add-box-line:before {content: "\ea0d";}.ri-add-circle-fill:before {content: "\ea0e";}.ri-add-circle-line:before {content: "\ea0f";}.ri-add-fill:before {content: "\ea10";}.ri-add-line:before {content: "\ea11";}.ri-admin-fill:before {content: "\ea12";}.ri-admin-line:before {content: "\ea13";}.ri-advertisement-fill:before {content: "\ea14";}.ri-advertisement-line:before {content: "\ea15";}.ri-airplay-fill:before {content: "\ea16";}.ri-airplay-line:before {content: "\ea17";}.ri-alarm-fill:before {content: "\ea18";}.ri-alarm-line:before {content: "\ea19";}.ri-alarm-warning-fill:before {content: "\ea1a";}.ri-alarm-warning-line:before {content: "\ea1b";}.ri-album-fill:before {content: "\ea1c";}.ri-album-line:before {content: "\ea1d";}.ri-alert-fill:before {content: "\ea1e";}.ri-alert-line:before {content: "\ea1f";}.ri-aliens-fill:before {content: "\ea20";}.ri-aliens-line:before {content: "\ea21";}.ri-align-bottom:before {content: "\ea22";}.ri-align-center:before {content: "\ea23";}.ri-align-justify:before {content: "\ea24";}.ri-align-left:before {content: "\ea25";}.ri-align-right:before {content: "\ea26";}.ri-align-top:before {content: "\ea27";}.ri-align-vertically:before {content: "\ea28";}.ri-alipay-fill:before {content: "\ea29";}.ri-alipay-line:before {content: "\ea2a";}.ri-amazon-fill:before {content: "\ea2b";}.ri-amazon-line:before {content: "\ea2c";}.ri-anchor-fill:before {content: "\ea2d";}.ri-anchor-line:before {content: "\ea2e";}.ri-ancient-gate-fill:before {content: "\ea2f";}.ri-ancient-gate-line:before {content: "\ea30";}.ri-ancient-pavilion-fill:before {content: "\ea31";}.ri-ancient-pavilion-line:before {content: "\ea32";}.ri-android-fill:before {content: "\ea33";}.ri-android-line:before {content: "\ea34";}.ri-angularjs-fill:before {content: "\ea35";}.ri-angularjs-line:before {content: "\ea36";}.ri-anticlockwise-2-fill:before {content: "\ea37";}.ri-anticlockwise-2-line:before {content: "\ea38";}.ri-anticlockwise-fill:before {content: "\ea39";}.ri-anticlockwise-line:before {content: "\ea3a";}.ri-app-store-fill:before {content: "\ea3b";}.ri-app-store-line:before {content: "\ea3c";}.ri-apple-fill:before {content: "\ea3d";}.ri-apple-line:before {content: "\ea3e";}.ri-apps-2-fill:before {content: "\ea3f";}.ri-apps-2-line:before {content: "\ea40";}.ri-apps-fill:before {content: "\ea41";}.ri-apps-line:before {content: "\ea42";}.ri-archive-drawer-fill:before {content: "\ea43";}.ri-archive-drawer-line:before {content: "\ea44";}.ri-archive-fill:before {content: "\ea45";}.ri-archive-line:before {content: "\ea46";}.ri-arrow-down-circle-fill:before {content: "\ea47";}.ri-arrow-down-circle-line:before {content: "\ea48";}.ri-arrow-down-fill:before {content: "\ea49";}.ri-arrow-down-line:before {content: "\ea4a";}.ri-arrow-down-s-fill:before {content: "\ea4b";}.ri-arrow-down-s-line:before {content: "\ea4c";}.ri-arrow-drop-down-fill:before {content: "\ea4d";}.ri-arrow-drop-down-line:before {content: "\ea4e";}.ri-arrow-drop-left-fill:before {content: "\ea4f";}.ri-arrow-drop-left-line:before {content: "\ea50";}.ri-arrow-drop-right-fill:before {content: "\ea51";}.ri-arrow-drop-right-line:before {content: "\ea52";}.ri-arrow-drop-up-fill:before {content: "\ea53";}.ri-arrow-drop-up-line:before {content: "\ea54";}.ri-arrow-go-back-fill:before {content: "\ea55";}.ri-arrow-go-back-line:before {content: "\ea56";}.ri-arrow-go-forward-fill:before {content: "\ea57";}.ri-arrow-go-forward-line:before {content: "\ea58";}.ri-arrow-left-circle-fill:before {content: "\ea59";}.ri-arrow-left-circle-line:before {content: "\ea5a";}.ri-arrow-left-down-fill:before {content: "\ea5b";}.ri-arrow-left-down-line:before {content: "\ea5c";}.ri-arrow-left-fill:before {content: "\ea5d";}.ri-arrow-left-line:before {content: "\ea5e";}.ri-arrow-left-right-fill:before {content: "\ea5f";}.ri-arrow-left-right-line:before {content: "\ea60";}.ri-arrow-left-s-fill:before {content: "\ea61";}.ri-arrow-left-s-line:before {content: "\ea62";}.ri-arrow-left-up-fill:before {content: "\ea63";}.ri-arrow-left-up-line:before {content: "\ea64";}.ri-arrow-right-circle-fill:before {content: "\ea65";}.ri-arrow-right-circle-line:before {content: "\ea66";}.ri-arrow-right-down-fill:before {content: "\ea67";}.ri-arrow-right-down-line:before {content: "\ea68";}.ri-arrow-right-fill:before {content: "\ea69";}.ri-arrow-right-line:before {content: "\ea6a";}.ri-arrow-right-s-fill:before {content: "\ea6b";}.ri-arrow-right-s-line:before {content: "\ea6c";}.ri-arrow-right-up-fill:before {content: "\ea6d";}.ri-arrow-right-up-line:before {content: "\ea6e";}.ri-arrow-up-circle-fill:before {content: "\ea6f";}.ri-arrow-up-circle-line:before {content: "\ea70";}.ri-arrow-up-down-fill:before {content: "\ea71";}.ri-arrow-up-down-line:before {content: "\ea72";}.ri-arrow-up-fill:before {content: "\ea73";}.ri-arrow-up-line:before {content: "\ea74";}.ri-arrow-up-s-fill:before {content: "\ea75";}.ri-arrow-up-s-line:before {content: "\ea76";}.ri-artboard-2-fill:before {content: "\ea77";}.ri-artboard-2-line:before {content: "\ea78";}.ri-artboard-fill:before {content: "\ea79";}.ri-artboard-line:before {content: "\ea7a";}.ri-article-fill:before {content: "\ea7b";}.ri-article-line:before {content: "\ea7c";}.ri-aspect-ratio-fill:before {content: "\ea7d";}.ri-aspect-ratio-line:before {content: "\ea7e";}.ri-asterisk:before {content: "\ea7f";}.ri-at-fill:before {content: "\ea80";}.ri-at-line:before {content: "\ea81";}.ri-attachment-2:before {content: "\ea82";}.ri-attachment-fill:before {content: "\ea83";}.ri-attachment-line:before {content: "\ea84";}.ri-auction-fill:before {content: "\ea85";}.ri-auction-line:before {content: "\ea86";}.ri-award-fill:before {content: "\ea87";}.ri-award-line:before {content: "\ea88";}.ri-baidu-fill:before {content: "\ea89";}.ri-baidu-line:before {content: "\ea8a";}.ri-ball-pen-fill:before {content: "\ea8b";}.ri-ball-pen-line:before {content: "\ea8c";}.ri-bank-card-2-fill:before {content: "\ea8d";}.ri-bank-card-2-line:before {content: "\ea8e";}.ri-bank-card-fill:before {content: "\ea8f";}.ri-bank-card-line:before {content: "\ea90";}.ri-bank-fill:before {content: "\ea91";}.ri-bank-line:before {content: "\ea92";}.ri-bar-chart-2-fill:before {content: "\ea93";}.ri-bar-chart-2-line:before {content: "\ea94";}.ri-bar-chart-box-fill:before {content: "\ea95";}.ri-bar-chart-box-line:before {content: "\ea96";}.ri-bar-chart-fill:before {content: "\ea97";}.ri-bar-chart-grouped-fill:before {content: "\ea98";}.ri-bar-chart-grouped-line:before {content: "\ea99";}.ri-bar-chart-horizontal-fill:before {content: "\ea9a";}.ri-bar-chart-horizontal-line:before {content: "\ea9b";}.ri-bar-chart-line:before {content: "\ea9c";}.ri-barcode-box-fill:before {content: "\ea9d";}.ri-barcode-box-line:before {content: "\ea9e";}.ri-barcode-fill:before {content: "\ea9f";}.ri-barcode-line:before {content: "\eaa0";}.ri-barricade-fill:before {content: "\eaa1";}.ri-barricade-line:before {content: "\eaa2";}.ri-base-station-fill:before {content: "\eaa3";}.ri-base-station-line:before {content: "\eaa4";}.ri-basketball-fill:before {content: "\eaa5";}.ri-basketball-line:before {content: "\eaa6";}.ri-battery-2-charge-fill:before {content: "\eaa7";}.ri-battery-2-charge-line:before {content: "\eaa8";}.ri-battery-2-fill:before {content: "\eaa9";}.ri-battery-2-line:before {content: "\eaaa";}.ri-battery-charge-fill:before {content: "\eaab";}.ri-battery-charge-line:before {content: "\eaac";}.ri-battery-fill:before {content: "\eaad";}.ri-battery-line:before {content: "\eaae";}.ri-battery-low-fill:before {content: "\eaaf";}.ri-battery-low-line:before {content: "\eab0";}.ri-battery-saver-fill:before {content: "\eab1";}.ri-battery-saver-line:before {content: "\eab2";}.ri-battery-share-fill:before {content: "\eab3";}.ri-battery-share-line:before {content: "\eab4";}.ri-bear-smile-fill:before {content: "\eab5";}.ri-bear-smile-line:before {content: "\eab6";}.ri-behance-fill:before {content: "\eab7";}.ri-behance-line:before {content: "\eab8";}.ri-bell-fill:before {content: "\eab9";}.ri-bell-line:before {content: "\eaba";}.ri-bike-fill:before {content: "\eabb";}.ri-bike-line:before {content: "\eabc";}.ri-bilibili-fill:before {content: "\eabd";}.ri-bilibili-line:before {content: "\eabe";}.ri-bill-fill:before {content: "\eabf";}.ri-bill-line:before {content: "\eac0";}.ri-billiards-fill:before {content: "\eac1";}.ri-billiards-line:before {content: "\eac2";}.ri-bit-coin-fill:before {content: "\eac3";}.ri-bit-coin-line:before {content: "\eac4";}.ri-blaze-fill:before {content: "\eac5";}.ri-blaze-line:before {content: "\eac6";}.ri-bluetooth-connect-fill:before {content: "\eac7";}.ri-bluetooth-connect-line:before {content: "\eac8";}.ri-bluetooth-fill:before {content: "\eac9";}.ri-bluetooth-line:before {content: "\eaca";}.ri-blur-off-fill:before {content: "\eacb";}.ri-blur-off-line:before {content: "\eacc";}.ri-body-scan-fill:before {content: "\eacd";}.ri-body-scan-line:before {content: "\eace";}.ri-bold:before {content: "\eacf";}.ri-book-2-fill:before {content: "\ead0";}.ri-book-2-line:before {content: "\ead1";}.ri-book-3-fill:before {content: "\ead2";}.ri-book-3-line:before {content: "\ead3";}.ri-book-fill:before {content: "\ead4";}.ri-book-line:before {content: "\ead5";}.ri-book-mark-fill:before {content: "\ead6";}.ri-book-mark-line:before {content: "\ead7";}.ri-book-open-fill:before {content: "\ead8";}.ri-book-open-line:before {content: "\ead9";}.ri-book-read-fill:before {content: "\eada";}.ri-book-read-line:before {content: "\eadb";}.ri-booklet-fill:before {content: "\eadc";}.ri-booklet-line:before {content: "\eadd";}.ri-bookmark-2-fill:before {content: "\eade";}.ri-bookmark-2-line:before {content: "\eadf";}.ri-bookmark-3-fill:before {content: "\eae0";}.ri-bookmark-3-line:before {content: "\eae1";}.ri-bookmark-fill:before {content: "\eae2";}.ri-bookmark-line:before {content: "\eae3";}.ri-boxing-fill:before {content: "\eae4";}.ri-boxing-line:before {content: "\eae5";}.ri-braces-fill:before {content: "\eae6";}.ri-braces-line:before {content: "\eae7";}.ri-brackets-fill:before {content: "\eae8";}.ri-brackets-line:before {content: "\eae9";}.ri-briefcase-2-fill:before {content: "\eaea";}.ri-briefcase-2-line:before {content: "\eaeb";}.ri-briefcase-3-fill:before {content: "\eaec";}.ri-briefcase-3-line:before {content: "\eaed";}.ri-briefcase-4-fill:before {content: "\eaee";}.ri-briefcase-4-line:before {content: "\eaef";}.ri-briefcase-5-fill:before {content: "\eaf0";}.ri-briefcase-5-line:before {content: "\eaf1";}.ri-briefcase-fill:before {content: "\eaf2";}.ri-briefcase-line:before {content: "\eaf3";}.ri-broadcast-fill:before {content: "\eaf4";}.ri-broadcast-line:before {content: "\eaf5";}.ri-brush-2-fill:before {content: "\eaf6";}.ri-brush-2-line:before {content: "\eaf7";}.ri-brush-3-fill:before {content: "\eaf8";}.ri-brush-3-line:before {content: "\eaf9";}.ri-brush-4-fill:before {content: "\eafa";}.ri-brush-4-line:before {content: "\eafb";}.ri-brush-fill:before {content: "\eafc";}.ri-brush-line:before {content: "\eafd";}.ri-bug-2-fill:before {content: "\eafe";}.ri-bug-2-line:before {content: "\eaff";}.ri-bug-fill:before {content: "\eb00";}.ri-bug-line:before {content: "\eb01";}.ri-building-2-fill:before {content: "\eb02";}.ri-building-2-line:before {content: "\eb03";}.ri-building-3-fill:before {content: "\eb04";}.ri-building-3-line:before {content: "\eb05";}.ri-building-4-fill:before {content: "\eb06";}.ri-building-4-line:before {content: "\eb07";}.ri-building-fill:before {content: "\eb08";}.ri-building-line:before {content: "\eb09";}.ri-bus-2-fill:before {content: "\eb0a";}.ri-bus-2-line:before {content: "\eb0b";}.ri-bus-fill:before {content: "\eb0c";}.ri-bus-line:before {content: "\eb0d";}.ri-bus-wifi-fill:before {content: "\eb0e";}.ri-bus-wifi-line:before {content: "\eb0f";}.ri-cake-2-fill:before {content: "\eb10";}.ri-cake-2-line:before {content: "\eb11";}.ri-cake-3-fill:before {content: "\eb12";}.ri-cake-3-line:before {content: "\eb13";}.ri-cake-fill:before {content: "\eb14";}.ri-cake-line:before {content: "\eb15";}.ri-calculator-fill:before {content: "\eb16";}.ri-calculator-line:before {content: "\eb17";}.ri-calendar-2-fill:before {content: "\eb18";}.ri-calendar-2-line:before {content: "\eb19";}.ri-calendar-check-fill:before {content: "\eb1a";}.ri-calendar-check-line:before {content: "\eb1b";}.ri-calendar-event-fill:before {content: "\eb1c";}.ri-calendar-event-line:before {content: "\eb1d";}.ri-calendar-fill:before {content: "\eb1e";}.ri-calendar-line:before {content: "\eb1f";}.ri-calendar-todo-fill:before {content: "\eb20";}.ri-calendar-todo-line:before {content: "\eb21";}.ri-camera-2-fill:before {content: "\eb22";}.ri-camera-2-line:before {content: "\eb23";}.ri-camera-3-fill:before {content: "\eb24";}.ri-camera-3-line:before {content: "\eb25";}.ri-camera-fill:before {content: "\eb26";}.ri-camera-lens-fill:before {content: "\eb27";}.ri-camera-lens-line:before {content: "\eb28";}.ri-camera-line:before {content: "\eb29";}.ri-camera-off-fill:before {content: "\eb2a";}.ri-camera-off-line:before {content: "\eb2b";}.ri-camera-switch-fill:before {content: "\eb2c";}.ri-camera-switch-line:before {content: "\eb2d";}.ri-car-fill:before {content: "\eb2e";}.ri-car-line:before {content: "\eb2f";}.ri-car-washing-fill:before {content: "\eb30";}.ri-car-washing-line:before {content: "\eb31";}.ri-cast-fill:before {content: "\eb32";}.ri-cast-line:before {content: "\eb33";}.ri-cellphone-fill:before {content: "\eb34";}.ri-cellphone-line:before {content: "\eb35";}.ri-celsius-fill:before {content: "\eb36";}.ri-celsius-line:before {content: "\eb37";}.ri-character-recognition-fill:before {content: "\eb38";}.ri-character-recognition-line:before {content: "\eb39";}.ri-charging-pile-2-fill:before {content: "\eb3a";}.ri-charging-pile-2-line:before {content: "\eb3b";}.ri-charging-pile-fill:before {content: "\eb3c";}.ri-charging-pile-line:before {content: "\eb3d";}.ri-chat-1-fill:before {content: "\eb3e";}.ri-chat-1-line:before {content: "\eb3f";}.ri-chat-2-fill:before {content: "\eb40";}.ri-chat-2-line:before {content: "\eb41";}.ri-chat-3-fill:before {content: "\eb42";}.ri-chat-3-line:before {content: "\eb43";}.ri-chat-4-fill:before {content: "\eb44";}.ri-chat-4-line:before {content: "\eb45";}.ri-chat-check-fill:before {content: "\eb46";}.ri-chat-check-line:before {content: "\eb47";}.ri-chat-delete-fill:before {content: "\eb48";}.ri-chat-delete-line:before {content: "\eb49";}.ri-chat-download-fill:before {content: "\eb4a";}.ri-chat-download-line:before {content: "\eb4b";}.ri-chat-forward-fill:before {content: "\eb4c";}.ri-chat-forward-line:before {content: "\eb4d";}.ri-chat-heart-fill:before {content: "\eb4e";}.ri-chat-heart-line:before {content: "\eb4f";}.ri-chat-new-fill:before {content: "\eb50";}.ri-chat-new-line:before {content: "\eb51";}.ri-chat-off-fill:before {content: "\eb52";}.ri-chat-off-line:before {content: "\eb53";}.ri-chat-settings-fill:before {content: "\eb54";}.ri-chat-settings-line:before {content: "\eb55";}.ri-chat-smile-2-fill:before {content: "\eb56";}.ri-chat-smile-2-line:before {content: "\eb57";}.ri-chat-smile-3-fill:before {content: "\eb58";}.ri-chat-smile-3-line:before {content: "\eb59";}.ri-chat-smile-fill:before {content: "\eb5a";}.ri-chat-smile-line:before {content: "\eb5b";}.ri-chat-upload-fill:before {content: "\eb5c";}.ri-chat-upload-line:before {content: "\eb5d";}.ri-chat-voice-fill:before {content: "\eb5e";}.ri-chat-voice-line:before {content: "\eb5f";}.ri-check-double-fill:before {content: "\eb60";}.ri-check-double-line:before {content: "\eb61";}.ri-check-fill:before {content: "\eb62";}.ri-check-line:before {content: "\eb63";}.ri-checkbox-blank-circle-fill:before {content: "\eb64";}.ri-checkbox-blank-circle-line:before {content: "\eb65";}.ri-checkbox-blank-fill:before {content: "\eb66";}.ri-checkbox-blank-line:before {content: "\eb67";}.ri-checkbox-circle-fill:before {content: "\eb68";}.ri-checkbox-circle-line:before {content: "\eb69";}.ri-checkbox-fill:before {content: "\eb6a";}.ri-checkbox-indeterminate-fill:before {content: "\eb6b";}.ri-checkbox-indeterminate-line:before {content: "\eb6c";}.ri-checkbox-line:before {content: "\eb6d";}.ri-checkbox-multiple-blank-fill:before {content: "\eb6e";}.ri-checkbox-multiple-blank-line:before {content: "\eb6f";}.ri-checkbox-multiple-fill:before {content: "\eb70";}.ri-checkbox-multiple-line:before {content: "\eb71";}.ri-china-railway-fill:before {content: "\eb72";}.ri-china-railway-line:before {content: "\eb73";}.ri-chrome-fill:before {content: "\eb74";}.ri-chrome-line:before {content: "\eb75";}.ri-clapperboard-fill:before {content: "\eb76";}.ri-clapperboard-line:before {content: "\eb77";}.ri-clipboard-fill:before {content: "\eb78";}.ri-clipboard-line:before {content: "\eb79";}.ri-clockwise-2-fill:before {content: "\eb7a";}.ri-clockwise-2-line:before {content: "\eb7b";}.ri-clockwise-fill:before {content: "\eb7c";}.ri-clockwise-line:before {content: "\eb7d";}.ri-close-circle-fill:before {content: "\eb7e";}.ri-close-circle-line:before {content: "\eb7f";}.ri-close-fill:before {content: "\eb80";}.ri-close-line:before {content: "\eb81";}.ri-cloud-fill:before {content: "\eb82";}.ri-cloud-line:before {content: "\eb83";}.ri-cloud-off-fill:before {content: "\eb84";}.ri-cloud-off-line:before {content: "\eb85";}.ri-cloud-windy-fill:before {content: "\eb86";}.ri-cloud-windy-line:before {content: "\eb87";}.ri-cloudy-2-fill:before {content: "\eb88";}.ri-cloudy-2-line:before {content: "\eb89";}.ri-cloudy-fill:before {content: "\eb8a";}.ri-cloudy-line:before {content: "\eb8b";}.ri-code-box-fill:before {content: "\eb8c";}.ri-code-box-line:before {content: "\eb8d";}.ri-code-fill:before {content: "\eb8e";}.ri-code-line:before {content: "\eb8f";}.ri-code-s-fill:before {content: "\eb90";}.ri-code-s-line:before {content: "\eb91";}.ri-code-s-slash-fill:before {content: "\eb92";}.ri-code-s-slash-line:before {content: "\eb93";}.ri-code-view:before {content: "\eb94";}.ri-codepen-fill:before {content: "\eb95";}.ri-codepen-line:before {content: "\eb96";}.ri-coin-fill:before {content: "\eb97";}.ri-coin-line:before {content: "\eb98";}.ri-coins-fill:before {content: "\eb99";}.ri-coins-line:before {content: "\eb9a";}.ri-command-fill:before {content: "\eb9b";}.ri-command-line:before {content: "\eb9c";}.ri-community-fill:before {content: "\eb9d";}.ri-community-line:before {content: "\eb9e";}.ri-compass-2-fill:before {content: "\eb9f";}.ri-compass-2-line:before {content: "\eba0";}.ri-compass-3-fill:before {content: "\eba1";}.ri-compass-3-line:before {content: "\eba2";}.ri-compass-4-fill:before {content: "\eba3";}.ri-compass-4-line:before {content: "\eba4";}.ri-compass-discover-fill:before {content: "\eba5";}.ri-compass-discover-line:before {content: "\eba6";}.ri-compass-fill:before {content: "\eba7";}.ri-compass-line:before {content: "\eba8";}.ri-compasses-2-fill:before {content: "\eba9";}.ri-compasses-2-line:before {content: "\ebaa";}.ri-compasses-fill:before {content: "\ebab";}.ri-compasses-line:before {content: "\ebac";}.ri-computer-fill:before {content: "\ebad";}.ri-computer-line:before {content: "\ebae";}.ri-contacts-book-2-fill:before {content: "\ebaf";}.ri-contacts-book-2-line:before {content: "\ebb0";}.ri-contacts-book-fill:before {content: "\ebb1";}.ri-contacts-book-line:before {content: "\ebb2";}.ri-contacts-book-upload-fill:before {content: "\ebb3";}.ri-contacts-book-upload-line:before {content: "\ebb4";}.ri-contacts-fill:before {content: "\ebb5";}.ri-contacts-line:before {content: "\ebb6";}.ri-contrast-2-fill:before {content: "\ebb7";}.ri-contrast-2-line:before {content: "\ebb8";}.ri-contrast-drop-2-fill:before {content: "\ebb9";}.ri-contrast-drop-2-line:before {content: "\ebba";}.ri-contrast-drop-fill:before {content: "\ebbb";}.ri-contrast-drop-line:before {content: "\ebbc";}.ri-contrast-fill:before {content: "\ebbd";}.ri-contrast-line:before {content: "\ebbe";}.ri-copper-coin-fill:before {content: "\ebbf";}.ri-copper-coin-line:before {content: "\ebc0";}.ri-copper-diamond-fill:before {content: "\ebc1";}.ri-copper-diamond-line:before {content: "\ebc2";}.ri-copyright-fill:before {content: "\ebc3";}.ri-copyright-line:before {content: "\ebc4";}.ri-coreos-fill:before {content: "\ebc5";}.ri-coreos-line:before {content: "\ebc6";}.ri-coupon-2-fill:before {content: "\ebc7";}.ri-coupon-2-line:before {content: "\ebc8";}.ri-coupon-3-fill:before {content: "\ebc9";}.ri-coupon-3-line:before {content: "\ebca";}.ri-coupon-4-fill:before {content: "\ebcb";}.ri-coupon-4-line:before {content: "\ebcc";}.ri-coupon-5-fill:before {content: "\ebcd";}.ri-coupon-5-line:before {content: "\ebce";}.ri-coupon-fill:before {content: "\ebcf";}.ri-coupon-line:before {content: "\ebd0";}.ri-cpu-fill:before {content: "\ebd1";}.ri-cpu-line:before {content: "\ebd2";}.ri-creative-commons-by-fill:before {content: "\ebd3";}.ri-creative-commons-by-line:before {content: "\ebd4";}.ri-creative-commons-fill:before {content: "\ebd5";}.ri-creative-commons-line:before {content: "\ebd6";}.ri-creative-commons-nc-fill:before {content: "\ebd7";}.ri-creative-commons-nc-line:before {content: "\ebd8";}.ri-creative-commons-nd-fill:before {content: "\ebd9";}.ri-creative-commons-nd-line:before {content: "\ebda";}.ri-creative-commons-sa-fill:before {content: "\ebdb";}.ri-creative-commons-sa-line:before {content: "\ebdc";}.ri-creative-commons-zero-fill:before {content: "\ebdd";}.ri-creative-commons-zero-line:before {content: "\ebde";}.ri-criminal-fill:before {content: "\ebdf";}.ri-criminal-line:before {content: "\ebe0";}.ri-crop-2-fill:before {content: "\ebe1";}.ri-crop-2-line:before {content: "\ebe2";}.ri-crop-fill:before {content: "\ebe3";}.ri-crop-line:before {content: "\ebe4";}.ri-css3-fill:before {content: "\ebe5";}.ri-css3-line:before {content: "\ebe6";}.ri-cup-fill:before {content: "\ebe7";}.ri-cup-line:before {content: "\ebe8";}.ri-currency-fill:before {content: "\ebe9";}.ri-currency-line:before {content: "\ebea";}.ri-cursor-fill:before {content: "\ebeb";}.ri-cursor-line:before {content: "\ebec";}.ri-customer-service-2-fill:before {content: "\ebed";}.ri-customer-service-2-line:before {content: "\ebee";}.ri-customer-service-fill:before {content: "\ebef";}.ri-customer-service-line:before {content: "\ebf0";}.ri-dashboard-fill:before {content: "\ebf1";}.ri-dashboard-line:before {content: "\ebf2";}.ri-database-2-fill:before {content: "\ebf3";}.ri-database-2-line:before {content: "\ebf4";}.ri-database-fill:before {content: "\ebf5";}.ri-database-line:before {content: "\ebf6";}.ri-delete-back-2-fill:before {content: "\ebf7";}.ri-delete-back-2-line:before {content: "\ebf8";}.ri-delete-back-fill:before {content: "\ebf9";}.ri-delete-back-line:before {content: "\ebfa";}.ri-delete-bin-2-fill:before {content: "\ebfb";}.ri-delete-bin-2-line:before {content: "\ebfc";}.ri-delete-bin-3-fill:before {content: "\ebfd";}.ri-delete-bin-3-line:before {content: "\ebfe";}.ri-delete-bin-4-fill:before {content: "\ebff";}.ri-delete-bin-4-line:before {content: "\ec00";}.ri-delete-bin-5-fill:before {content: "\ec01";}.ri-delete-bin-5-line:before {content: "\ec02";}.ri-delete-bin-6-fill:before {content: "\ec03";}.ri-delete-bin-6-line:before {content: "\ec04";}.ri-delete-bin-7-fill:before {content: "\ec05";}.ri-delete-bin-7-line:before {content: "\ec06";}.ri-delete-bin-fill:before {content: "\ec07";}.ri-delete-bin-line:before {content: "\ec08";}.ri-device-fill:before {content: "\ec09";}.ri-device-line:before {content: "\ec0a";}.ri-device-recover-fill:before {content: "\ec0b";}.ri-device-recover-line:before {content: "\ec0c";}.ri-dingding-fill:before {content: "\ec0d";}.ri-dingding-line:before {content: "\ec0e";}.ri-direction-fill:before {content: "\ec0f";}.ri-direction-line:before {content: "\ec10";}.ri-disc-fill:before {content: "\ec11";}.ri-disc-line:before {content: "\ec12";}.ri-discord-fill:before {content: "\ec13";}.ri-discord-line:before {content: "\ec14";}.ri-discuss-fill:before {content: "\ec15";}.ri-discuss-line:before {content: "\ec16";}.ri-divide-fill:before {content: "\ec17";}.ri-divide-line:before {content: "\ec18";}.ri-door-lock-box-fill:before {content: "\ec19";}.ri-door-lock-box-line:before {content: "\ec1a";}.ri-door-lock-fill:before {content: "\ec1b";}.ri-door-lock-line:before {content: "\ec1c";}.ri-douban-fill:before {content: "\ec1d";}.ri-douban-line:before {content: "\ec1e";}.ri-double-quotes-l:before {content: "\ec1f";}.ri-double-quotes-r:before {content: "\ec20";}.ri-download-2-fill:before {content: "\ec21";}.ri-download-2-line:before {content: "\ec22";}.ri-download-cloud-2-fill:before {content: "\ec23";}.ri-download-cloud-2-line:before {content: "\ec24";}.ri-download-cloud-fill:before {content: "\ec25";}.ri-download-cloud-line:before {content: "\ec26";}.ri-download-fill:before {content: "\ec27";}.ri-download-line:before {content: "\ec28";}.ri-drag-drop-fill:before {content: "\ec29";}.ri-drag-drop-line:before {content: "\ec2a";}.ri-drag-move-2-fill:before {content: "\ec2b";}.ri-drag-move-2-line:before {content: "\ec2c";}.ri-drag-move-fill:before {content: "\ec2d";}.ri-drag-move-line:before {content: "\ec2e";}.ri-dribbble-fill:before {content: "\ec2f";}.ri-dribbble-line:before {content: "\ec30";}.ri-drive-fill:before {content: "\ec31";}.ri-drive-line:before {content: "\ec32";}.ri-drizzle-fill:before {content: "\ec33";}.ri-drizzle-line:before {content: "\ec34";}.ri-drop-fill:before {content: "\ec35";}.ri-drop-line:before {content: "\ec36";}.ri-dropbox-fill:before {content: "\ec37";}.ri-dropbox-line:before {content: "\ec38";}.ri-dual-sim-1-fill:before {content: "\ec39";}.ri-dual-sim-1-line:before {content: "\ec3a";}.ri-dual-sim-2-fill:before {content: "\ec3b";}.ri-dual-sim-2-line:before {content: "\ec3c";}.ri-dv-fill:before {content: "\ec3d";}.ri-dv-line:before {content: "\ec3e";}.ri-dvd-fill:before {content: "\ec3f";}.ri-dvd-line:before {content: "\ec40";}.ri-e-bike-2-fill:before {content: "\ec41";}.ri-e-bike-2-line:before {content: "\ec42";}.ri-e-bike-fill:before {content: "\ec43";}.ri-e-bike-line:before {content: "\ec44";}.ri-earth-fill:before {content: "\ec45";}.ri-earth-line:before {content: "\ec46";}.ri-earthquake-fill:before {content: "\ec47";}.ri-earthquake-line:before {content: "\ec48";}.ri-edge-fill:before {content: "\ec49";}.ri-edge-line:before {content: "\ec4a";}.ri-edit-2-fill:before {content: "\ec4b";}.ri-edit-2-line:before {content: "\ec4c";}.ri-edit-box-fill:before {content: "\ec4d";}.ri-edit-box-line:before {content: "\ec4e";}.ri-edit-circle-fill:before {content: "\ec4f";}.ri-edit-circle-line:before {content: "\ec50";}.ri-edit-fill:before {content: "\ec51";}.ri-edit-line:before {content: "\ec52";}.ri-eject-fill:before {content: "\ec53";}.ri-eject-line:before {content: "\ec54";}.ri-emotion-2-fill:before {content: "\ec55";}.ri-emotion-2-line:before {content: "\ec56";}.ri-emotion-fill:before {content: "\ec57";}.ri-emotion-happy-fill:before {content: "\ec58";}.ri-emotion-happy-line:before {content: "\ec59";}.ri-emotion-laugh-fill:before {content: "\ec5a";}.ri-emotion-laugh-line:before {content: "\ec5b";}.ri-emotion-line:before {content: "\ec5c";}.ri-emotion-normal-fill:before {content: "\ec5d";}.ri-emotion-normal-line:before {content: "\ec5e";}.ri-emotion-sad-fill:before {content: "\ec5f";}.ri-emotion-sad-line:before {content: "\ec60";}.ri-emotion-unhappy-fill:before {content: "\ec61";}.ri-emotion-unhappy-line:before {content: "\ec62";}.ri-emphasis-cn:before {content: "\ec63";}.ri-emphasis:before {content: "\ec64";}.ri-english-input:before {content: "\ec65";}.ri-equalizer-fill:before {content: "\ec66";}.ri-equalizer-line:before {content: "\ec67";}.ri-eraser-fill:before {content: "\ec68";}.ri-eraser-line:before {content: "\ec69";}.ri-error-warning-fill:before {content: "\ec6a";}.ri-error-warning-line:before {content: "\ec6b";}.ri-evernote-fill:before {content: "\ec6c";}.ri-evernote-line:before {content: "\ec6d";}.ri-exchange-box-fill:before {content: "\ec6e";}.ri-exchange-box-line:before {content: "\ec6f";}.ri-exchange-cny-fill:before {content: "\ec70";}.ri-exchange-cny-line:before {content: "\ec71";}.ri-exchange-dollar-fill:before {content: "\ec72";}.ri-exchange-dollar-line:before {content: "\ec73";}.ri-exchange-fill:before {content: "\ec74";}.ri-exchange-funds-fill:before {content: "\ec75";}.ri-exchange-funds-line:before {content: "\ec76";}.ri-exchange-line:before {content: "\ec77";}.ri-external-link-fill:before {content: "\ec78";}.ri-external-link-line:before {content: "\ec79";}.ri-eye-2-fill:before {content: "\ec7a";}.ri-eye-2-line:before {content: "\ec7b";}.ri-eye-close-fill:before {content: "\ec7c";}.ri-eye-close-line:before {content: "\ec7d";}.ri-eye-fill:before {content: "\ec7e";}.ri-eye-line:before {content: "\ec7f";}.ri-eye-off-fill:before {content: "\ec80";}.ri-eye-off-line:before {content: "\ec81";}.ri-facebook-box-fill:before {content: "\ec82";}.ri-facebook-box-line:before {content: "\ec83";}.ri-facebook-circle-fill:before {content: "\ec84";}.ri-facebook-circle-line:before {content: "\ec85";}.ri-facebook-fill:before {content: "\ec86";}.ri-facebook-line:before {content: "\ec87";}.ri-fahrenheit-fill:before {content: "\ec88";}.ri-fahrenheit-line:before {content: "\ec89";}.ri-feedback-fill:before {content: "\ec8a";}.ri-feedback-line:before {content: "\ec8b";}.ri-file-2-fill:before {content: "\ec8c";}.ri-file-2-line:before {content: "\ec8d";}.ri-file-3-fill:before {content: "\ec8e";}.ri-file-3-line:before {content: "\ec8f";}.ri-file-4-fill:before {content: "\ec90";}.ri-file-4-line:before {content: "\ec91";}.ri-file-add-fill:before {content: "\ec92";}.ri-file-add-line:before {content: "\ec93";}.ri-file-chart-2-fill:before {content: "\ec94";}.ri-file-chart-2-line:before {content: "\ec95";}.ri-file-chart-fill:before {content: "\ec96";}.ri-file-chart-line:before {content: "\ec97";}.ri-file-cloud-fill:before {content: "\ec98";}.ri-file-cloud-line:before {content: "\ec99";}.ri-file-code-fill:before {content: "\ec9a";}.ri-file-code-line:before {content: "\ec9b";}.ri-file-copy-2-fill:before {content: "\ec9c";}.ri-file-copy-2-line:before {content: "\ec9d";}.ri-file-copy-fill:before {content: "\ec9e";}.ri-file-copy-line:before {content: "\ec9f";}.ri-file-damage-fill:before {content: "\eca0";}.ri-file-damage-line:before {content: "\eca1";}.ri-file-download-fill:before {content: "\eca2";}.ri-file-download-line:before {content: "\eca3";}.ri-file-edit-fill:before {content: "\eca4";}.ri-file-edit-line:before {content: "\eca5";}.ri-file-excel-2-fill:before {content: "\eca6";}.ri-file-excel-2-line:before {content: "\eca7";}.ri-file-excel-fill:before {content: "\eca8";}.ri-file-excel-line:before {content: "\eca9";}.ri-file-fill:before {content: "\ecaa";}.ri-file-forbid-fill:before {content: "\ecab";}.ri-file-forbid-line:before {content: "\ecac";}.ri-file-hwp-fill:before {content: "\ecad";}.ri-file-hwp-line:before {content: "\ecae";}.ri-file-info-fill:before {content: "\ecaf";}.ri-file-info-line:before {content: "\ecb0";}.ri-file-line:before {content: "\ecb1";}.ri-file-list-2-fill:before {content: "\ecb2";}.ri-file-list-2-line:before {content: "\ecb3";}.ri-file-list-3-fill:before {content: "\ecb4";}.ri-file-list-3-line:before {content: "\ecb5";}.ri-file-list-fill:before {content: "\ecb6";}.ri-file-list-line:before {content: "\ecb7";}.ri-file-lock-fill:before {content: "\ecb8";}.ri-file-lock-line:before {content: "\ecb9";}.ri-file-mark-fill:before {content: "\ecba";}.ri-file-mark-line:before {content: "\ecbb";}.ri-file-music-fill:before {content: "\ecbc";}.ri-file-music-line:before {content: "\ecbd";}.ri-file-paper-2-fill:before {content: "\ecbe";}.ri-file-paper-2-line:before {content: "\ecbf";}.ri-file-paper-fill:before {content: "\ecc0";}.ri-file-paper-line:before {content: "\ecc1";}.ri-file-pdf-fill:before {content: "\ecc2";}.ri-file-pdf-line:before {content: "\ecc3";}.ri-file-ppt-2-fill:before {content: "\ecc4";}.ri-file-ppt-2-line:before {content: "\ecc5";}.ri-file-ppt-fill:before {content: "\ecc6";}.ri-file-ppt-line:before {content: "\ecc7";}.ri-file-reduce-fill:before {content: "\ecc8";}.ri-file-reduce-line:before {content: "\ecc9";}.ri-file-search-fill:before {content: "\ecca";}.ri-file-search-line:before {content: "\eccb";}.ri-file-settings-fill:before {content: "\eccc";}.ri-file-settings-line:before {content: "\eccd";}.ri-file-shield-2-fill:before {content: "\ecce";}.ri-file-shield-2-line:before {content: "\eccf";}.ri-file-shield-fill:before {content: "\ecd0";}.ri-file-shield-line:before {content: "\ecd1";}.ri-file-shred-fill:before {content: "\ecd2";}.ri-file-shred-line:before {content: "\ecd3";}.ri-file-text-fill:before {content: "\ecd4";}.ri-file-text-line:before {content: "\ecd5";}.ri-file-transfer-fill:before {content: "\ecd6";}.ri-file-transfer-line:before {content: "\ecd7";}.ri-file-unknow-fill:before {content: "\ecd8";}.ri-file-unknow-line:before {content: "\ecd9";}.ri-file-upload-fill:before {content: "\ecda";}.ri-file-upload-line:before {content: "\ecdb";}.ri-file-user-fill:before {content: "\ecdc";}.ri-file-user-line:before {content: "\ecdd";}.ri-file-warning-fill:before {content: "\ecde";}.ri-file-warning-line:before {content: "\ecdf";}.ri-file-word-2-fill:before {content: "\ece0";}.ri-file-word-2-line:before {content: "\ece1";}.ri-file-word-fill:before {content: "\ece2";}.ri-file-word-line:before {content: "\ece3";}.ri-file-zip-fill:before {content: "\ece4";}.ri-file-zip-line:before {content: "\ece5";}.ri-film-fill:before {content: "\ece6";}.ri-film-line:before {content: "\ece7";}.ri-filter-2-fill:before {content: "\ece8";}.ri-filter-2-line:before {content: "\ece9";}.ri-filter-3-fill:before {content: "\ecea";}.ri-filter-3-line:before {content: "\eceb";}.ri-filter-fill:before {content: "\ecec";}.ri-filter-line:before {content: "\eced";}.ri-find-replace-fill:before {content: "\ecee";}.ri-find-replace-line:before {content: "\ecef";}.ri-fingerprint-2-fill:before {content: "\ecf0";}.ri-fingerprint-2-line:before {content: "\ecf1";}.ri-fingerprint-fill:before {content: "\ecf2";}.ri-fingerprint-line:before {content: "\ecf3";}.ri-fire-fill:before {content: "\ecf4";}.ri-fire-line:before {content: "\ecf5";}.ri-firefox-fill:before {content: "\ecf6";}.ri-firefox-line:before {content: "\ecf7";}.ri-flag-2-fill:before {content: "\ecf8";}.ri-flag-2-line:before {content: "\ecf9";}.ri-flag-fill:before {content: "\ecfa";}.ri-flag-line:before {content: "\ecfb";}.ri-flashlight-fill:before {content: "\ecfc";}.ri-flashlight-line:before {content: "\ecfd";}.ri-flask-fill:before {content: "\ecfe";}.ri-flask-line:before {content: "\ecff";}.ri-flight-land-fill:before {content: "\ed00";}.ri-flight-land-line:before {content: "\ed01";}.ri-flight-takeoff-fill:before {content: "\ed02";}.ri-flight-takeoff-line:before {content: "\ed03";}.ri-flood-fill:before {content: "\ed04";}.ri-flood-line:before {content: "\ed05";}.ri-flutter-fill:before {content: "\ed06";}.ri-flutter-line:before {content: "\ed07";}.ri-focus-2-fill:before {content: "\ed08";}.ri-focus-2-line:before {content: "\ed09";}.ri-focus-3-fill:before {content: "\ed0a";}.ri-focus-3-line:before {content: "\ed0b";}.ri-focus-fill:before {content: "\ed0c";}.ri-focus-line:before {content: "\ed0d";}.ri-foggy-fill:before {content: "\ed0e";}.ri-foggy-line:before {content: "\ed0f";}.ri-folder-2-fill:before {content: "\ed10";}.ri-folder-2-line:before {content: "\ed11";}.ri-folder-3-fill:before {content: "\ed12";}.ri-folder-3-line:before {content: "\ed13";}.ri-folder-4-fill:before {content: "\ed14";}.ri-folder-4-line:before {content: "\ed15";}.ri-folder-5-fill:before {content: "\ed16";}.ri-folder-5-line:before {content: "\ed17";}.ri-folder-add-fill:before {content: "\ed18";}.ri-folder-add-line:before {content: "\ed19";}.ri-folder-chart-2-fill:before {content: "\ed1a";}.ri-folder-chart-2-line:before {content: "\ed1b";}.ri-folder-chart-fill:before {content: "\ed1c";}.ri-folder-chart-line:before {content: "\ed1d";}.ri-folder-download-fill:before {content: "\ed1e";}.ri-folder-download-line:before {content: "\ed1f";}.ri-folder-fill:before {content: "\ed20";}.ri-folder-forbid-fill:before {content: "\ed21";}.ri-folder-forbid-line:before {content: "\ed22";}.ri-folder-info-fill:before {content: "\ed23";}.ri-folder-info-line:before {content: "\ed24";}.ri-folder-keyhole-fill:before {content: "\ed25";}.ri-folder-keyhole-line:before {content: "\ed26";}.ri-folder-line:before {content: "\ed27";}.ri-folder-lock-fill:before {content: "\ed28";}.ri-folder-lock-line:before {content: "\ed29";}.ri-folder-music-fill:before {content: "\ed2a";}.ri-folder-music-line:before {content: "\ed2b";}.ri-folder-open-fill:before {content: "\ed2c";}.ri-folder-open-line:before {content: "\ed2d";}.ri-folder-received-fill:before {content: "\ed2e";}.ri-folder-received-line:before {content: "\ed2f";}.ri-folder-reduce-fill:before {content: "\ed30";}.ri-folder-reduce-line:before {content: "\ed31";}.ri-folder-settings-fill:before {content: "\ed32";}.ri-folder-settings-line:before {content: "\ed33";}.ri-folder-shared-fill:before {content: "\ed34";}.ri-folder-shared-line:before {content: "\ed35";}.ri-folder-shield-2-fill:before {content: "\ed36";}.ri-folder-shield-2-line:before {content: "\ed37";}.ri-folder-shield-fill:before {content: "\ed38";}.ri-folder-shield-line:before {content: "\ed39";}.ri-folder-transfer-fill:before {content: "\ed3a";}.ri-folder-transfer-line:before {content: "\ed3b";}.ri-folder-unknow-fill:before {content: "\ed3c";}.ri-folder-unknow-line:before {content: "\ed3d";}.ri-folder-upload-fill:before {content: "\ed3e";}.ri-folder-upload-line:before {content: "\ed3f";}.ri-folder-user-fill:before {content: "\ed40";}.ri-folder-user-line:before {content: "\ed41";}.ri-folder-warning-fill:before {content: "\ed42";}.ri-folder-warning-line:before {content: "\ed43";}.ri-folder-zip-fill:before {content: "\ed44";}.ri-folder-zip-line:before {content: "\ed45";}.ri-folders-fill:before {content: "\ed46";}.ri-folders-line:before {content: "\ed47";}.ri-font-color:before {content: "\ed48";}.ri-font-size-2:before {content: "\ed49";}.ri-font-size:before {content: "\ed4a";}.ri-football-fill:before {content: "\ed4b";}.ri-football-line:before {content: "\ed4c";}.ri-footprint-fill:before {content: "\ed4d";}.ri-footprint-line:before {content: "\ed4e";}.ri-forbid-2-fill:before {content: "\ed4f";}.ri-forbid-2-line:before {content: "\ed50";}.ri-forbid-fill:before {content: "\ed51";}.ri-forbid-line:before {content: "\ed52";}.ri-format-clear:before {content: "\ed53";}.ri-fullscreen-exit-fill:before {content: "\ed54";}.ri-fullscreen-exit-line:before {content: "\ed55";}.ri-fullscreen-fill:before {content: "\ed56";}.ri-fullscreen-line:before {content: "\ed57";}.ri-function-fill:before {content: "\ed58";}.ri-function-line:before {content: "\ed59";}.ri-functions:before {content: "\ed5a";}.ri-funds-box-fill:before {content: "\ed5b";}.ri-funds-box-line:before {content: "\ed5c";}.ri-funds-fill:before {content: "\ed5d";}.ri-funds-line:before {content: "\ed5e";}.ri-gallery-fill:before {content: "\ed5f";}.ri-gallery-line:before {content: "\ed60";}.ri-gallery-upload-fill:before {content: "\ed61";}.ri-gallery-upload-line:before {content: "\ed62";}.ri-game-fill:before {content: "\ed63";}.ri-game-line:before {content: "\ed64";}.ri-gamepad-fill:before {content: "\ed65";}.ri-gamepad-line:before {content: "\ed66";}.ri-gas-station-fill:before {content: "\ed67";}.ri-gas-station-line:before {content: "\ed68";}.ri-gatsby-fill:before {content: "\ed69";}.ri-gatsby-line:before {content: "\ed6a";}.ri-genderless-fill:before {content: "\ed6b";}.ri-genderless-line:before {content: "\ed6c";}.ri-ghost-2-fill:before {content: "\ed6d";}.ri-ghost-2-line:before {content: "\ed6e";}.ri-ghost-fill:before {content: "\ed6f";}.ri-ghost-line:before {content: "\ed70";}.ri-ghost-smile-fill:before {content: "\ed71";}.ri-ghost-smile-line:before {content: "\ed72";}.ri-gift-2-fill:before {content: "\ed73";}.ri-gift-2-line:before {content: "\ed74";}.ri-gift-fill:before {content: "\ed75";}.ri-gift-line:before {content: "\ed76";}.ri-git-branch-fill:before {content: "\ed77";}.ri-git-branch-line:before {content: "\ed78";}.ri-git-commit-fill:before {content: "\ed79";}.ri-git-commit-line:before {content: "\ed7a";}.ri-git-merge-fill:before {content: "\ed7b";}.ri-git-merge-line:before {content: "\ed7c";}.ri-git-pull-request-fill:before {content: "\ed7d";}.ri-git-pull-request-line:before {content: "\ed7e";}.ri-git-repository-commits-fill:before {content: "\ed7f";}.ri-git-repository-commits-line:before {content: "\ed80";}.ri-git-repository-fill:before {content: "\ed81";}.ri-git-repository-line:before {content: "\ed82";}.ri-git-repository-private-fill:before {content: "\ed83";}.ri-git-repository-private-line:before {content: "\ed84";}.ri-github-fill:before {content: "\ed85";}.ri-github-line:before {content: "\ed86";}.ri-gitlab-fill:before {content: "\ed87";}.ri-gitlab-line:before {content: "\ed88";}.ri-global-fill:before {content: "\ed89";}.ri-global-line:before {content: "\ed8a";}.ri-globe-fill:before {content: "\ed8b";}.ri-globe-line:before {content: "\ed8c";}.ri-goblet-fill:before {content: "\ed8d";}.ri-goblet-line:before {content: "\ed8e";}.ri-google-fill:before {content: "\ed8f";}.ri-google-line:before {content: "\ed90";}.ri-google-play-fill:before {content: "\ed91";}.ri-google-play-line:before {content: "\ed92";}.ri-government-fill:before {content: "\ed93";}.ri-government-line:before {content: "\ed94";}.ri-gps-fill:before {content: "\ed95";}.ri-gps-line:before {content: "\ed96";}.ri-gradienter-fill:before {content: "\ed97";}.ri-gradienter-line:before {content: "\ed98";}.ri-grid-fill:before {content: "\ed99";}.ri-grid-line:before {content: "\ed9a";}.ri-group-2-fill:before {content: "\ed9b";}.ri-group-2-line:before {content: "\ed9c";}.ri-group-fill:before {content: "\ed9d";}.ri-group-line:before {content: "\ed9e";}.ri-guide-fill:before {content: "\ed9f";}.ri-guide-line:before {content: "\eda0";}.ri-hail-fill:before {content: "\eda1";}.ri-hail-line:before {content: "\eda2";}.ri-hammer-fill:before {content: "\eda3";}.ri-hammer-line:before {content: "\eda4";}.ri-hand-coin-fill:before {content: "\eda5";}.ri-hand-coin-line:before {content: "\eda6";}.ri-hand-heart-fill:before {content: "\eda7";}.ri-hand-heart-line:before {content: "\eda8";}.ri-handbag-fill:before {content: "\eda9";}.ri-handbag-line:before {content: "\edaa";}.ri-hard-drive-2-fill:before {content: "\edab";}.ri-hard-drive-2-line:before {content: "\edac";}.ri-hard-drive-fill:before {content: "\edad";}.ri-hard-drive-line:before {content: "\edae";}.ri-hashtag:before {content: "\edaf";}.ri-haze-2-fill:before {content: "\edb0";}.ri-haze-2-line:before {content: "\edb1";}.ri-haze-fill:before {content: "\edb2";}.ri-haze-line:before {content: "\edb3";}.ri-hd-fill:before {content: "\edb4";}.ri-hd-line:before {content: "\edb5";}.ri-heading:before {content: "\edb6";}.ri-headphone-fill:before {content: "\edb7";}.ri-headphone-line:before {content: "\edb8";}.ri-heart-2-fill:before {content: "\edb9";}.ri-heart-2-line:before {content: "\edba";}.ri-heart-add-fill:before {content: "\edbb";}.ri-heart-add-line:before {content: "\edbc";}.ri-heart-fill:before {content: "\edbd";}.ri-heart-line:before {content: "\edbe";}.ri-hearts-fill:before {content: "\edbf";}.ri-hearts-line:before {content: "\edc0";}.ri-heavy-showers-fill:before {content: "\edc1";}.ri-heavy-showers-line:before {content: "\edc2";}.ri-home-2-fill:before {content: "\edc3";}.ri-home-2-line:before {content: "\edc4";}.ri-home-3-fill:before {content: "\edc5";}.ri-home-3-line:before {content: "\edc6";}.ri-home-4-fill:before {content: "\edc7";}.ri-home-4-line:before {content: "\edc8";}.ri-home-5-fill:before {content: "\edc9";}.ri-home-5-line:before {content: "\edca";}.ri-home-6-fill:before {content: "\edcb";}.ri-home-6-line:before {content: "\edcc";}.ri-home-7-fill:before {content: "\edcd";}.ri-home-7-line:before {content: "\edce";}.ri-home-8-fill:before {content: "\edcf";}.ri-home-8-line:before {content: "\edd0";}.ri-home-fill:before {content: "\edd1";}.ri-home-gear-fill:before {content: "\edd2";}.ri-home-gear-line:before {content: "\edd3";}.ri-home-heart-fill:before {content: "\edd4";}.ri-home-heart-line:before {content: "\edd5";}.ri-home-line:before {content: "\edd6";}.ri-home-smile-2-fill:before {content: "\edd7";}.ri-home-smile-2-line:before {content: "\edd8";}.ri-home-smile-fill:before {content: "\edd9";}.ri-home-smile-line:before {content: "\edda";}.ri-home-wifi-fill:before {content: "\eddb";}.ri-home-wifi-line:before {content: "\eddc";}.ri-honour-fill:before {content: "\eddd";}.ri-honour-line:before {content: "\edde";}.ri-hospital-fill:before {content: "\eddf";}.ri-hospital-line:before {content: "\ede0";}.ri-hotel-bed-fill:before {content: "\ede1";}.ri-hotel-bed-line:before {content: "\ede2";}.ri-hotel-fill:before {content: "\ede3";}.ri-hotel-line:before {content: "\ede4";}.ri-hotspot-fill:before {content: "\ede5";}.ri-hotspot-line:before {content: "\ede6";}.ri-hq-fill:before {content: "\ede7";}.ri-hq-line:before {content: "\ede8";}.ri-html5-fill:before {content: "\ede9";}.ri-html5-line:before {content: "\edea";}.ri-ie-fill:before {content: "\edeb";}.ri-ie-line:before {content: "\edec";}.ri-image-2-fill:before {content: "\eded";}.ri-image-2-line:before {content: "\edee";}.ri-image-add-fill:before {content: "\edef";}.ri-image-add-line:before {content: "\edf0";}.ri-image-fill:before {content: "\edf1";}.ri-image-line:before {content: "\edf2";}.ri-inbox-archive-fill:before {content: "\edf3";}.ri-inbox-archive-line:before {content: "\edf4";}.ri-inbox-fill:before {content: "\edf5";}.ri-inbox-line:before {content: "\edf6";}.ri-inbox-unarchive-fill:before {content: "\edf7";}.ri-inbox-unarchive-line:before {content: "\edf8";}.ri-increase-decrease-fill:before {content: "\edf9";}.ri-increase-decrease-line:before {content: "\edfa";}.ri-indent-decrease:before {content: "\edfb";}.ri-indent-increase:before {content: "\edfc";}.ri-indeterminate-circle-fill:before {content: "\edfd";}.ri-indeterminate-circle-line:before {content: "\edfe";}.ri-information-fill:before {content: "\edff";}.ri-information-line:before {content: "\ee00";}.ri-input-cursor-move:before {content: "\ee01";}.ri-input-method-fill:before {content: "\ee02";}.ri-input-method-line:before {content: "\ee03";}.ri-instagram-fill:before {content: "\ee04";}.ri-instagram-line:before {content: "\ee05";}.ri-install-fill:before {content: "\ee06";}.ri-install-line:before {content: "\ee07";}.ri-invision-fill:before {content: "\ee08";}.ri-invision-line:before {content: "\ee09";}.ri-italic:before {content: "\ee0a";}.ri-kakao-talk-fill:before {content: "\ee0b";}.ri-kakao-talk-line:before {content: "\ee0c";}.ri-key-2-fill:before {content: "\ee0d";}.ri-key-2-line:before {content: "\ee0e";}.ri-key-fill:before {content: "\ee0f";}.ri-key-line:before {content: "\ee10";}.ri-keyboard-box-fill:before {content: "\ee11";}.ri-keyboard-box-line:before {content: "\ee12";}.ri-keyboard-fill:before {content: "\ee13";}.ri-keyboard-line:before {content: "\ee14";}.ri-keynote-fill:before {content: "\ee15";}.ri-keynote-line:before {content: "\ee16";}.ri-knife-blood-fill:before {content: "\ee17";}.ri-knife-blood-line:before {content: "\ee18";}.ri-knife-fill:before {content: "\ee19";}.ri-knife-line:before {content: "\ee1a";}.ri-landscape-fill:before {content: "\ee1b";}.ri-landscape-line:before {content: "\ee1c";}.ri-layout-2-fill:before {content: "\ee1d";}.ri-layout-2-line:before {content: "\ee1e";}.ri-layout-3-fill:before {content: "\ee1f";}.ri-layout-3-line:before {content: "\ee20";}.ri-layout-4-fill:before {content: "\ee21";}.ri-layout-4-line:before {content: "\ee22";}.ri-layout-5-fill:before {content: "\ee23";}.ri-layout-5-line:before {content: "\ee24";}.ri-layout-6-fill:before {content: "\ee25";}.ri-layout-6-line:before {content: "\ee26";}.ri-layout-bottom-2-fill:before {content: "\ee27";}.ri-layout-bottom-2-line:before {content: "\ee28";}.ri-layout-bottom-fill:before {content: "\ee29";}.ri-layout-bottom-line:before {content: "\ee2a";}.ri-layout-column-fill:before {content: "\ee2b";}.ri-layout-column-line:before {content: "\ee2c";}.ri-layout-fill:before {content: "\ee2d";}.ri-layout-grid-fill:before {content: "\ee2e";}.ri-layout-grid-line:before {content: "\ee2f";}.ri-layout-left-2-fill:before {content: "\ee30";}.ri-layout-left-2-line:before {content: "\ee31";}.ri-layout-left-fill:before {content: "\ee32";}.ri-layout-left-line:before {content: "\ee33";}.ri-layout-line:before {content: "\ee34";}.ri-layout-masonry-fill:before {content: "\ee35";}.ri-layout-masonry-line:before {content: "\ee36";}.ri-layout-right-2-fill:before {content: "\ee37";}.ri-layout-right-2-line:before {content: "\ee38";}.ri-layout-right-fill:before {content: "\ee39";}.ri-layout-right-line:before {content: "\ee3a";}.ri-layout-row-fill:before {content: "\ee3b";}.ri-layout-row-line:before {content: "\ee3c";}.ri-layout-top-2-fill:before {content: "\ee3d";}.ri-layout-top-2-line:before {content: "\ee3e";}.ri-layout-top-fill:before {content: "\ee3f";}.ri-layout-top-line:before {content: "\ee40";}.ri-lifebuoy-fill:before {content: "\ee41";}.ri-lifebuoy-line:before {content: "\ee42";}.ri-lightbulb-fill:before {content: "\ee43";}.ri-lightbulb-flash-fill:before {content: "\ee44";}.ri-lightbulb-flash-line:before {content: "\ee45";}.ri-lightbulb-line:before {content: "\ee46";}.ri-line-fill:before {content: "\ee47";}.ri-line-height:before {content: "\ee48";}.ri-line-line:before {content: "\ee49";}.ri-link-m:before {content: "\ee4a";}.ri-link-unlink-m:before {content: "\ee4b";}.ri-link-unlink:before {content: "\ee4c";}.ri-link:before {content: "\ee4d";}.ri-linkedin-box-fill:before {content: "\ee4e";}.ri-linkedin-box-line:before {content: "\ee4f";}.ri-linkedin-fill:before {content: "\ee50";}.ri-linkedin-line:before {content: "\ee51";}.ri-links-fill:before {content: "\ee52";}.ri-links-line:before {content: "\ee53";}.ri-list-check-2:before {content: "\ee54";}.ri-list-check:before {content: "\ee55";}.ri-list-ordered:before {content: "\ee56";}.ri-list-settings-fill:before {content: "\ee57";}.ri-list-settings-line:before {content: "\ee58";}.ri-list-unordered:before {content: "\ee59";}.ri-live-fill:before {content: "\ee5a";}.ri-live-line:before {content: "\ee5b";}.ri-loader-2-fill:before {content: "\ee5c";}.ri-loader-2-line:before {content: "\ee5d";}.ri-loader-3-fill:before {content: "\ee5e";}.ri-loader-3-line:before {content: "\ee5f";}.ri-loader-4-fill:before {content: "\ee60";}.ri-loader-4-line:before {content: "\ee61";}.ri-loader-5-fill:before {content: "\ee62";}.ri-loader-5-line:before {content: "\ee63";}.ri-loader-fill:before {content: "\ee64";}.ri-loader-line:before {content: "\ee65";}.ri-lock-2-fill:before {content: "\ee66";}.ri-lock-2-line:before {content: "\ee67";}.ri-lock-fill:before {content: "\ee68";}.ri-lock-line:before {content: "\ee69";}.ri-lock-password-fill:before {content: "\ee6a";}.ri-lock-password-line:before {content: "\ee6b";}.ri-lock-unlock-fill:before {content: "\ee6c";}.ri-lock-unlock-line:before {content: "\ee6d";}.ri-login-box-fill:before {content: "\ee6e";}.ri-login-box-line:before {content: "\ee6f";}.ri-login-circle-fill:before {content: "\ee70";}.ri-login-circle-line:before {content: "\ee71";}.ri-logout-box-fill:before {content: "\ee72";}.ri-logout-box-line:before {content: "\ee73";}.ri-logout-box-r-fill:before {content: "\ee74";}.ri-logout-box-r-line:before {content: "\ee75";}.ri-logout-circle-fill:before {content: "\ee76";}.ri-logout-circle-line:before {content: "\ee77";}.ri-logout-circle-r-fill:before {content: "\ee78";}.ri-logout-circle-r-line:before {content: "\ee79";}.ri-mac-fill:before {content: "\ee7a";}.ri-mac-line:before {content: "\ee7b";}.ri-macbook-fill:before {content: "\ee7c";}.ri-macbook-line:before {content: "\ee7d";}.ri-magic-fill:before {content: "\ee7e";}.ri-magic-line:before {content: "\ee7f";}.ri-mail-add-fill:before {content: "\ee80";}.ri-mail-add-line:before {content: "\ee81";}.ri-mail-check-fill:before {content: "\ee82";}.ri-mail-check-line:before {content: "\ee83";}.ri-mail-close-fill:before {content: "\ee84";}.ri-mail-close-line:before {content: "\ee85";}.ri-mail-download-fill:before {content: "\ee86";}.ri-mail-download-line:before {content: "\ee87";}.ri-mail-fill:before {content: "\ee88";}.ri-mail-forbid-fill:before {content: "\ee89";}.ri-mail-forbid-line:before {content: "\ee8a";}.ri-mail-line:before {content: "\ee8b";}.ri-mail-lock-fill:before {content: "\ee8c";}.ri-mail-lock-line:before {content: "\ee8d";}.ri-mail-open-fill:before {content: "\ee8e";}.ri-mail-open-line:before {content: "\ee8f";}.ri-mail-send-fill:before {content: "\ee90";}.ri-mail-send-line:before {content: "\ee91";}.ri-mail-settings-fill:before {content: "\ee92";}.ri-mail-settings-line:before {content: "\ee93";}.ri-mail-star-fill:before {content: "\ee94";}.ri-mail-star-line:before {content: "\ee95";}.ri-mail-unread-fill:before {content: "\ee96";}.ri-mail-unread-line:before {content: "\ee97";}.ri-mail-volume-fill:before {content: "\ee98";}.ri-mail-volume-line:before {content: "\ee99";}.ri-map-2-fill:before {content: "\ee9a";}.ri-map-2-line:before {content: "\ee9b";}.ri-map-fill:before {content: "\ee9c";}.ri-map-line:before {content: "\ee9d";}.ri-map-pin-2-fill:before {content: "\ee9e";}.ri-map-pin-2-line:before {content: "\ee9f";}.ri-map-pin-3-fill:before {content: "\eea0";}.ri-map-pin-3-line:before {content: "\eea1";}.ri-map-pin-4-fill:before {content: "\eea2";}.ri-map-pin-4-line:before {content: "\eea3";}.ri-map-pin-5-fill:before {content: "\eea4";}.ri-map-pin-5-line:before {content: "\eea5";}.ri-map-pin-add-fill:before {content: "\eea6";}.ri-map-pin-add-line:before {content: "\eea7";}.ri-map-pin-fill:before {content: "\eea8";}.ri-map-pin-line:before {content: "\eea9";}.ri-map-pin-range-fill:before {content: "\eeaa";}.ri-map-pin-range-line:before {content: "\eeab";}.ri-map-pin-time-fill:before {content: "\eeac";}.ri-map-pin-time-line:before {content: "\eead";}.ri-map-pin-user-fill:before {content: "\eeae";}.ri-map-pin-user-line:before {content: "\eeaf";}.ri-mark-pen-fill:before {content: "\eeb0";}.ri-mark-pen-line:before {content: "\eeb1";}.ri-markdown-fill:before {content: "\eeb2";}.ri-markdown-line:before {content: "\eeb3";}.ri-markup-fill:before {content: "\eeb4";}.ri-markup-line:before {content: "\eeb5";}.ri-mastercard-fill:before {content: "\eeb6";}.ri-mastercard-line:before {content: "\eeb7";}.ri-mastodon-fill:before {content: "\eeb8";}.ri-mastodon-line:before {content: "\eeb9";}.ri-medal-2-fill:before {content: "\eeba";}.ri-medal-2-line:before {content: "\eebb";}.ri-medal-fill:before {content: "\eebc";}.ri-medal-line:before {content: "\eebd";}.ri-medium-fill:before {content: "\eebe";}.ri-medium-line:before {content: "\eebf";}.ri-men-fill:before {content: "\eec0";}.ri-men-line:before {content: "\eec1";}.ri-menu-2-fill:before {content: "\eec2";}.ri-menu-2-line:before {content: "\eec3";}.ri-menu-3-fill:before {content: "\eec4";}.ri-menu-3-line:before {content: "\eec5";}.ri-menu-4-fill:before {content: "\eec6";}.ri-menu-4-line:before {content: "\eec7";}.ri-menu-5-fill:before {content: "\eec8";}.ri-menu-5-line:before {content: "\eec9";}.ri-menu-add-fill:before {content: "\eeca";}.ri-menu-add-line:before {content: "\eecb";}.ri-menu-fill:before {content: "\eecc";}.ri-menu-line:before {content: "\eecd";}.ri-message-2-fill:before {content: "\eece";}.ri-message-2-line:before {content: "\eecf";}.ri-message-3-fill:before {content: "\eed0";}.ri-message-3-line:before {content: "\eed1";}.ri-message-fill:before {content: "\eed2";}.ri-message-line:before {content: "\eed3";}.ri-messenger-fill:before {content: "\eed4";}.ri-messenger-line:before {content: "\eed5";}.ri-meteor-fill:before {content: "\eed6";}.ri-meteor-line:before {content: "\eed7";}.ri-mic-2-fill:before {content: "\eed8";}.ri-mic-2-line:before {content: "\eed9";}.ri-mic-fill:before {content: "\eeda";}.ri-mic-line:before {content: "\eedb";}.ri-mic-off-fill:before {content: "\eedc";}.ri-mic-off-line:before {content: "\eedd";}.ri-mickey-fill:before {content: "\eede";}.ri-mickey-line:before {content: "\eedf";}.ri-mini-program-fill:before {content: "\eee0";}.ri-mini-program-line:before {content: "\eee1";}.ri-mist-fill:before {content: "\eee2";}.ri-mist-line:before {content: "\eee3";}.ri-money-cny-box-fill:before {content: "\eee4";}.ri-money-cny-box-line:before {content: "\eee5";}.ri-money-cny-circle-fill:before {content: "\eee6";}.ri-money-cny-circle-line:before {content: "\eee7";}.ri-money-dollar-box-fill:before {content: "\eee8";}.ri-money-dollar-box-line:before {content: "\eee9";}.ri-money-dollar-circle-fill:before {content: "\eeea";}.ri-money-dollar-circle-line:before {content: "\eeeb";}.ri-money-euro-box-fill:before {content: "\eeec";}.ri-money-euro-box-line:before {content: "\eeed";}.ri-money-euro-circle-fill:before {content: "\eeee";}.ri-money-euro-circle-line:before {content: "\eeef";}.ri-money-pound-box-fill:before {content: "\eef0";}.ri-money-pound-box-line:before {content: "\eef1";}.ri-money-pound-circle-fill:before {content: "\eef2";}.ri-money-pound-circle-line:before {content: "\eef3";}.ri-moon-clear-fill:before {content: "\eef4";}.ri-moon-clear-line:before {content: "\eef5";}.ri-moon-cloudy-fill:before {content: "\eef6";}.ri-moon-cloudy-line:before {content: "\eef7";}.ri-moon-fill:before {content: "\eef8";}.ri-moon-foggy-fill:before {content: "\eef9";}.ri-moon-foggy-line:before {content: "\eefa";}.ri-moon-line:before {content: "\eefb";}.ri-more-2-fill:before {content: "\eefc";}.ri-more-2-line:before {content: "\eefd";}.ri-more-fill:before {content: "\eefe";}.ri-more-line:before {content: "\eeff";}.ri-motorbike-fill:before {content: "\ef00";}.ri-motorbike-line:before {content: "\ef01";}.ri-mouse-fill:before {content: "\ef02";}.ri-mouse-line:before {content: "\ef03";}.ri-movie-2-fill:before {content: "\ef04";}.ri-movie-2-line:before {content: "\ef05";}.ri-movie-fill:before {content: "\ef06";}.ri-movie-line:before {content: "\ef07";}.ri-music-2-fill:before {content: "\ef08";}.ri-music-2-line:before {content: "\ef09";}.ri-music-fill:before {content: "\ef0a";}.ri-music-line:before {content: "\ef0b";}.ri-mv-fill:before {content: "\ef0c";}.ri-mv-line:before {content: "\ef0d";}.ri-navigation-fill:before {content: "\ef0e";}.ri-navigation-line:before {content: "\ef0f";}.ri-netease-cloud-music-fill:before {content: "\ef10";}.ri-netease-cloud-music-line:before {content: "\ef11";}.ri-netflix-fill:before {content: "\ef12";}.ri-netflix-line:before {content: "\ef13";}.ri-newspaper-fill:before {content: "\ef14";}.ri-newspaper-line:before {content: "\ef15";}.ri-notification-2-fill:before {content: "\ef16";}.ri-notification-2-line:before {content: "\ef17";}.ri-notification-3-fill:before {content: "\ef18";}.ri-notification-3-line:before {content: "\ef19";}.ri-notification-4-fill:before {content: "\ef1a";}.ri-notification-4-line:before {content: "\ef1b";}.ri-notification-badge-fill:before {content: "\ef1c";}.ri-notification-badge-line:before {content: "\ef1d";}.ri-notification-fill:before {content: "\ef1e";}.ri-notification-line:before {content: "\ef1f";}.ri-notification-off-fill:before {content: "\ef20";}.ri-notification-off-line:before {content: "\ef21";}.ri-number-0:before {content: "\ef22";}.ri-number-1:before {content: "\ef23";}.ri-number-2:before {content: "\ef24";}.ri-number-3:before {content: "\ef25";}.ri-number-4:before {content: "\ef26";}.ri-number-5:before {content: "\ef27";}.ri-number-6:before {content: "\ef28";}.ri-number-7:before {content: "\ef29";}.ri-number-8:before {content: "\ef2a";}.ri-number-9:before {content: "\ef2b";}.ri-numbers-fill:before {content: "\ef2c";}.ri-numbers-line:before {content: "\ef2d";}.ri-oil-fill:before {content: "\ef2e";}.ri-oil-line:before {content: "\ef2f";}.ri-omega:before {content: "\ef30";}.ri-open-arm-fill:before {content: "\ef31";}.ri-open-arm-line:before {content: "\ef32";}.ri-opera-fill:before {content: "\ef33";}.ri-opera-line:before {content: "\ef34";}.ri-order-play-fill:before {content: "\ef35";}.ri-order-play-line:before {content: "\ef36";}.ri-outlet-2-fill:before {content: "\ef37";}.ri-outlet-2-line:before {content: "\ef38";}.ri-outlet-fill:before {content: "\ef39";}.ri-outlet-line:before {content: "\ef3a";}.ri-page-separator:before {content: "\ef3b";}.ri-pages-fill:before {content: "\ef3c";}.ri-pages-line:before {content: "\ef3d";}.ri-paint-brush-fill:before {content: "\ef3e";}.ri-paint-brush-line:before {content: "\ef3f";}.ri-paint-fill:before {content: "\ef40";}.ri-paint-line:before {content: "\ef41";}.ri-palette-fill:before {content: "\ef42";}.ri-palette-line:before {content: "\ef43";}.ri-pantone-fill:before {content: "\ef44";}.ri-pantone-line:before {content: "\ef45";}.ri-paragraph:before {content: "\ef46";}.ri-parent-fill:before {content: "\ef47";}.ri-parent-line:before {content: "\ef48";}.ri-parentheses-fill:before {content: "\ef49";}.ri-parentheses-line:before {content: "\ef4a";}.ri-parking-box-fill:before {content: "\ef4b";}.ri-parking-box-line:before {content: "\ef4c";}.ri-parking-fill:before {content: "\ef4d";}.ri-parking-line:before {content: "\ef4e";}.ri-passport-fill:before {content: "\ef4f";}.ri-passport-line:before {content: "\ef50";}.ri-patreon-fill:before {content: "\ef51";}.ri-patreon-line:before {content: "\ef52";}.ri-pause-circle-fill:before {content: "\ef53";}.ri-pause-circle-line:before {content: "\ef54";}.ri-pause-fill:before {content: "\ef55";}.ri-pause-line:before {content: "\ef56";}.ri-pause-mini-fill:before {content: "\ef57";}.ri-pause-mini-line:before {content: "\ef58";}.ri-paypal-fill:before {content: "\ef59";}.ri-paypal-line:before {content: "\ef5a";}.ri-pen-nib-fill:before {content: "\ef5b";}.ri-pen-nib-line:before {content: "\ef5c";}.ri-pencil-fill:before {content: "\ef5d";}.ri-pencil-line:before {content: "\ef5e";}.ri-pencil-ruler-2-fill:before {content: "\ef5f";}.ri-pencil-ruler-2-line:before {content: "\ef60";}.ri-pencil-ruler-fill:before {content: "\ef61";}.ri-pencil-ruler-line:before {content: "\ef62";}.ri-percent-fill:before {content: "\ef63";}.ri-percent-line:before {content: "\ef64";}.ri-phone-camera-fill:before {content: "\ef65";}.ri-phone-camera-line:before {content: "\ef66";}.ri-phone-fill:before {content: "\ef67";}.ri-phone-find-fill:before {content: "\ef68";}.ri-phone-find-line:before {content: "\ef69";}.ri-phone-line:before {content: "\ef6a";}.ri-phone-lock-fill:before {content: "\ef6b";}.ri-phone-lock-line:before {content: "\ef6c";}.ri-picture-in-picture-2-fill:before {content: "\ef6d";}.ri-picture-in-picture-2-line:before {content: "\ef6e";}.ri-picture-in-picture-exit-fill:before {content: "\ef6f";}.ri-picture-in-picture-exit-line:before {content: "\ef70";}.ri-picture-in-picture-fill:before {content: "\ef71";}.ri-picture-in-picture-line:before {content: "\ef72";}.ri-pie-chart-2-fill:before {content: "\ef73";}.ri-pie-chart-2-line:before {content: "\ef74";}.ri-pie-chart-box-fill:before {content: "\ef75";}.ri-pie-chart-box-line:before {content: "\ef76";}.ri-pie-chart-fill:before {content: "\ef77";}.ri-pie-chart-line:before {content: "\ef78";}.ri-pin-distance-fill:before {content: "\ef79";}.ri-pin-distance-line:before {content: "\ef7a";}.ri-ping-pong-fill:before {content: "\ef7b";}.ri-ping-pong-line:before {content: "\ef7c";}.ri-pinterest-fill:before {content: "\ef7d";}.ri-pinterest-line:before {content: "\ef7e";}.ri-pinyin-input:before {content: "\ef7f";}.ri-plane-fill:before {content: "\ef80";}.ri-plane-line:before {content: "\ef81";}.ri-play-circle-fill:before {content: "\ef82";}.ri-play-circle-line:before {content: "\ef83";}.ri-play-fill:before {content: "\ef84";}.ri-play-line:before {content: "\ef85";}.ri-play-list-add-fill:before {content: "\ef86";}.ri-play-list-add-line:before {content: "\ef87";}.ri-play-list-fill:before {content: "\ef88";}.ri-play-list-line:before {content: "\ef89";}.ri-play-mini-fill:before {content: "\ef8a";}.ri-play-mini-line:before {content: "\ef8b";}.ri-playstation-fill:before {content: "\ef8c";}.ri-playstation-line:before {content: "\ef8d";}.ri-plug-2-fill:before {content: "\ef8e";}.ri-plug-2-line:before {content: "\ef8f";}.ri-plug-fill:before {content: "\ef90";}.ri-plug-line:before {content: "\ef91";}.ri-polaroid-2-fill:before {content: "\ef92";}.ri-polaroid-2-line:before {content: "\ef93";}.ri-polaroid-fill:before {content: "\ef94";}.ri-polaroid-line:before {content: "\ef95";}.ri-police-car-fill:before {content: "\ef96";}.ri-police-car-line:before {content: "\ef97";}.ri-price-tag-2-fill:before {content: "\ef98";}.ri-price-tag-2-line:before {content: "\ef99";}.ri-price-tag-3-fill:before {content: "\ef9a";}.ri-price-tag-3-line:before {content: "\ef9b";}.ri-price-tag-fill:before {content: "\ef9c";}.ri-price-tag-line:before {content: "\ef9d";}.ri-printer-cloud-fill:before {content: "\ef9e";}.ri-printer-cloud-line:before {content: "\ef9f";}.ri-printer-fill:before {content: "\efa0";}.ri-printer-line:before {content: "\efa1";}.ri-product-hunt-fill:before {content: "\efa2";}.ri-product-hunt-line:before {content: "\efa3";}.ri-profile-fill:before {content: "\efa4";}.ri-profile-line:before {content: "\efa5";}.ri-projector-2-fill:before {content: "\efa6";}.ri-projector-2-line:before {content: "\efa7";}.ri-projector-fill:before {content: "\efa8";}.ri-projector-line:before {content: "\efa9";}.ri-pushpin-2-fill:before {content: "\efaa";}.ri-pushpin-2-line:before {content: "\efab";}.ri-pushpin-fill:before {content: "\efac";}.ri-pushpin-line:before {content: "\efad";}.ri-qq-fill:before {content: "\efae";}.ri-qq-line:before {content: "\efaf";}.ri-qr-code-fill:before {content: "\efb0";}.ri-qr-code-line:before {content: "\efb1";}.ri-qr-scan-2-fill:before {content: "\efb2";}.ri-qr-scan-2-line:before {content: "\efb3";}.ri-qr-scan-fill:before {content: "\efb4";}.ri-qr-scan-line:before {content: "\efb5";}.ri-question-answer-fill:before {content: "\efb6";}.ri-question-answer-line:before {content: "\efb7";}.ri-question-fill:before {content: "\efb8";}.ri-question-line:before {content: "\efb9";}.ri-questionnaire-fill:before {content: "\efba";}.ri-questionnaire-line:before {content: "\efbb";}.ri-quill-pen-fill:before {content: "\efbc";}.ri-quill-pen-line:before {content: "\efbd";}.ri-radar-fill:before {content: "\efbe";}.ri-radar-line:before {content: "\efbf";}.ri-radio-2-fill:before {content: "\efc0";}.ri-radio-2-line:before {content: "\efc1";}.ri-radio-button-fill:before {content: "\efc2";}.ri-radio-button-line:before {content: "\efc3";}.ri-radio-fill:before {content: "\efc4";}.ri-radio-line:before {content: "\efc5";}.ri-rainbow-fill:before {content: "\efc6";}.ri-rainbow-line:before {content: "\efc7";}.ri-rainy-fill:before {content: "\efc8";}.ri-rainy-line:before {content: "\efc9";}.ri-reactjs-fill:before {content: "\efca";}.ri-reactjs-line:before {content: "\efcb";}.ri-record-circle-fill:before {content: "\efcc";}.ri-record-circle-line:before {content: "\efcd";}.ri-record-mail-fill:before {content: "\efce";}.ri-record-mail-line:before {content: "\efcf";}.ri-red-packet-fill:before {content: "\efd0";}.ri-red-packet-line:before {content: "\efd1";}.ri-reddit-fill:before {content: "\efd2";}.ri-reddit-line:before {content: "\efd3";}.ri-refresh-fill:before {content: "\efd4";}.ri-refresh-line:before {content: "\efd5";}.ri-refund-2-fill:before {content: "\efd6";}.ri-refund-2-line:before {content: "\efd7";}.ri-refund-fill:before {content: "\efd8";}.ri-refund-line:before {content: "\efd9";}.ri-registered-fill:before {content: "\efda";}.ri-registered-line:before {content: "\efdb";}.ri-remixicon-fill:before {content: "\efdc";}.ri-remixicon-line:before {content: "\efdd";}.ri-remote-control-2-fill:before {content: "\efde";}.ri-remote-control-2-line:before {content: "\efdf";}.ri-remote-control-fill:before {content: "\efe0";}.ri-remote-control-line:before {content: "\efe1";}.ri-repeat-2-fill:before {content: "\efe2";}.ri-repeat-2-line:before {content: "\efe3";}.ri-repeat-fill:before {content: "\efe4";}.ri-repeat-line:before {content: "\efe5";}.ri-repeat-one-fill:before {content: "\efe6";}.ri-repeat-one-line:before {content: "\efe7";}.ri-reply-fill:before {content: "\efe8";}.ri-reply-line:before {content: "\efe9";}.ri-reserved-fill:before {content: "\efea";}.ri-reserved-line:before {content: "\efeb";}.ri-restart-fill:before {content: "\efec";}.ri-restart-line:before {content: "\efed";}.ri-restaurant-2-fill:before {content: "\efee";}.ri-restaurant-2-line:before {content: "\efef";}.ri-restaurant-fill:before {content: "\eff0";}.ri-restaurant-line:before {content: "\eff1";}.ri-rewind-fill:before {content: "\eff2";}.ri-rewind-line:before {content: "\eff3";}.ri-rewind-mini-fill:before {content: "\eff4";}.ri-rewind-mini-line:before {content: "\eff5";}.ri-rhythm-fill:before {content: "\eff6";}.ri-rhythm-line:before {content: "\eff7";}.ri-riding-fill:before {content: "\eff8";}.ri-riding-line:before {content: "\eff9";}.ri-road-map-fill:before {content: "\effa";}.ri-road-map-line:before {content: "\effb";}.ri-roadster-fill:before {content: "\effc";}.ri-roadster-line:before {content: "\effd";}.ri-robot-fill:before {content: "\effe";}.ri-robot-line:before {content: "\efff";}.ri-rocket-2-fill:before {content: "\f000";}.ri-rocket-2-line:before {content: "\f001";}.ri-rocket-fill:before {content: "\f002";}.ri-rocket-line:before {content: "\f003";}.ri-rotate-lock-fill:before {content: "\f004";}.ri-rotate-lock-line:before {content: "\f005";}.ri-route-fill:before {content: "\f006";}.ri-route-line:before {content: "\f007";}.ri-router-fill:before {content: "\f008";}.ri-router-line:before {content: "\f009";}.ri-rss-fill:before {content: "\f00a";}.ri-rss-line:before {content: "\f00b";}.ri-ruler-2-fill:before {content: "\f00c";}.ri-ruler-2-line:before {content: "\f00d";}.ri-ruler-fill:before {content: "\f00e";}.ri-ruler-line:before {content: "\f00f";}.ri-run-fill:before {content: "\f010";}.ri-run-line:before {content: "\f011";}.ri-safari-fill:before {content: "\f012";}.ri-safari-line:before {content: "\f013";}.ri-safe-2-fill:before {content: "\f014";}.ri-safe-2-line:before {content: "\f015";}.ri-safe-fill:before {content: "\f016";}.ri-safe-line:before {content: "\f017";}.ri-sailboat-fill:before {content: "\f018";}.ri-sailboat-line:before {content: "\f019";}.ri-save-2-fill:before {content: "\f01a";}.ri-save-2-line:before {content: "\f01b";}.ri-save-3-fill:before {content: "\f01c";}.ri-save-3-line:before {content: "\f01d";}.ri-save-fill:before {content: "\f01e";}.ri-save-line:before {content: "\f01f";}.ri-scan-2-fill:before {content: "\f020";}.ri-scan-2-line:before {content: "\f021";}.ri-scan-fill:before {content: "\f022";}.ri-scan-line:before {content: "\f023";}.ri-scissors-2-fill:before {content: "\f024";}.ri-scissors-2-line:before {content: "\f025";}.ri-scissors-cut-fill:before {content: "\f026";}.ri-scissors-cut-line:before {content: "\f027";}.ri-scissors-fill:before {content: "\f028";}.ri-scissors-line:before {content: "\f029";}.ri-screenshot-2-fill:before {content: "\f02a";}.ri-screenshot-2-line:before {content: "\f02b";}.ri-screenshot-fill:before {content: "\f02c";}.ri-screenshot-line:before {content: "\f02d";}.ri-sd-card-fill:before {content: "\f02e";}.ri-sd-card-line:before {content: "\f02f";}.ri-sd-card-mini-fill:before {content: "\f030";}.ri-sd-card-mini-line:before {content: "\f031";}.ri-search-2-fill:before {content: "\f032";}.ri-search-2-line:before {content: "\f033";}.ri-search-eye-fill:before {content: "\f034";}.ri-search-eye-line:before {content: "\f035";}.ri-search-fill:before {content: "\f036";}.ri-search-line:before {content: "\f037";}.ri-secure-payment-fill:before {content: "\f038";}.ri-secure-payment-line:before {content: "\f039";}.ri-send-plane-2-fill:before {content: "\f03a";}.ri-send-plane-2-line:before {content: "\f03b";}.ri-send-plane-fill:before {content: "\f03c";}.ri-send-plane-line:before {content: "\f03d";}.ri-sensor-fill:before {content: "\f03e";}.ri-sensor-line:before {content: "\f03f";}.ri-separator:before {content: "\f040";}.ri-server-fill:before {content: "\f041";}.ri-server-line:before {content: "\f042";}.ri-service-fill:before {content: "\f043";}.ri-service-line:before {content: "\f044";}.ri-settings-2-fill:before {content: "\f045";}.ri-settings-2-line:before {content: "\f046";}.ri-settings-3-fill:before {content: "\f047";}.ri-settings-3-line:before {content: "\f048";}.ri-settings-4-fill:before {content: "\f049";}.ri-settings-4-line:before {content: "\f04a";}.ri-settings-5-fill:before {content: "\f04b";}.ri-settings-5-line:before {content: "\f04c";}.ri-settings-6-fill:before {content: "\f04d";}.ri-settings-6-line:before {content: "\f04e";}.ri-settings-fill:before {content: "\f04f";}.ri-settings-line:before {content: "\f050";}.ri-shape-2-fill:before {content: "\f051";}.ri-shape-2-line:before {content: "\f052";}.ri-shape-fill:before {content: "\f053";}.ri-shape-line:before {content: "\f054";}.ri-share-box-fill:before {content: "\f055";}.ri-share-box-line:before {content: "\f056";}.ri-share-circle-fill:before {content: "\f057";}.ri-share-circle-line:before {content: "\f058";}.ri-share-fill:before {content: "\f059";}.ri-share-forward-2-fill:before {content: "\f05a";}.ri-share-forward-2-line:before {content: "\f05b";}.ri-share-forward-box-fill:before {content: "\f05c";}.ri-share-forward-box-line:before {content: "\f05d";}.ri-share-forward-fill:before {content: "\f05e";}.ri-share-forward-line:before {content: "\f05f";}.ri-share-line:before {content: "\f060";}.ri-shield-cross-fill:before {content: "\f061";}.ri-shield-cross-line:before {content: "\f062";}.ri-shield-fill:before {content: "\f063";}.ri-shield-flash-fill:before {content: "\f064";}.ri-shield-flash-line:before {content: "\f065";}.ri-shield-keyhole-fill:before {content: "\f066";}.ri-shield-keyhole-line:before {content: "\f067";}.ri-shield-line:before {content: "\f068";}.ri-shield-star-fill:before {content: "\f069";}.ri-shield-star-line:before {content: "\f06a";}.ri-shield-user-fill:before {content: "\f06b";}.ri-shield-user-line:before {content: "\f06c";}.ri-ship-2-fill:before {content: "\f06d";}.ri-ship-2-line:before {content: "\f06e";}.ri-ship-fill:before {content: "\f06f";}.ri-ship-line:before {content: "\f070";}.ri-shirt-fill:before {content: "\f071";}.ri-shirt-line:before {content: "\f072";}.ri-shopping-bag-2-fill:before {content: "\f073";}.ri-shopping-bag-2-line:before {content: "\f074";}.ri-shopping-bag-3-fill:before {content: "\f075";}.ri-shopping-bag-3-line:before {content: "\f076";}.ri-shopping-bag-fill:before {content: "\f077";}.ri-shopping-bag-line:before {content: "\f078";}.ri-shopping-basket-2-fill:before {content: "\f079";}.ri-shopping-basket-2-line:before {content: "\f07a";}.ri-shopping-basket-fill:before {content: "\f07b";}.ri-shopping-basket-line:before {content: "\f07c";}.ri-shopping-cart-2-fill:before {content: "\f07d";}.ri-shopping-cart-2-line:before {content: "\f07e";}.ri-shopping-cart-fill:before {content: "\f07f";}.ri-shopping-cart-line:before {content: "\f080";}.ri-showers-fill:before {content: "\f081";}.ri-showers-line:before {content: "\f082";}.ri-shuffle-fill:before {content: "\f083";}.ri-shuffle-line:before {content: "\f084";}.ri-shut-down-fill:before {content: "\f085";}.ri-shut-down-line:before {content: "\f086";}.ri-side-bar-fill:before {content: "\f087";}.ri-side-bar-line:before {content: "\f088";}.ri-signal-tower-fill:before {content: "\f089";}.ri-signal-tower-line:before {content: "\f08a";}.ri-sim-card-2-fill:before {content: "\f08b";}.ri-sim-card-2-line:before {content: "\f08c";}.ri-sim-card-fill:before {content: "\f08d";}.ri-sim-card-line:before {content: "\f08e";}.ri-single-quotes-l:before {content: "\f08f";}.ri-single-quotes-r:before {content: "\f090";}.ri-sip-fill:before {content: "\f091";}.ri-sip-line:before {content: "\f092";}.ri-skip-back-fill:before {content: "\f093";}.ri-skip-back-line:before {content: "\f094";}.ri-skip-back-mini-fill:before {content: "\f095";}.ri-skip-back-mini-line:before {content: "\f096";}.ri-skip-forward-fill:before {content: "\f097";}.ri-skip-forward-line:before {content: "\f098";}.ri-skip-forward-mini-fill:before {content: "\f099";}.ri-skip-forward-mini-line:before {content: "\f09a";}.ri-skull-2-fill:before {content: "\f09b";}.ri-skull-2-line:before {content: "\f09c";}.ri-skull-fill:before {content: "\f09d";}.ri-skull-line:before {content: "\f09e";}.ri-skype-fill:before {content: "\f09f";}.ri-skype-line:before {content: "\f0a0";}.ri-slack-fill:before {content: "\f0a1";}.ri-slack-line:before {content: "\f0a2";}.ri-slice-fill:before {content: "\f0a3";}.ri-slice-line:before {content: "\f0a4";}.ri-slideshow-2-fill:before {content: "\f0a5";}.ri-slideshow-2-line:before {content: "\f0a6";}.ri-slideshow-3-fill:before {content: "\f0a7";}.ri-slideshow-3-line:before {content: "\f0a8";}.ri-slideshow-4-fill:before {content: "\f0a9";}.ri-slideshow-4-line:before {content: "\f0aa";}.ri-slideshow-fill:before {content: "\f0ab";}.ri-slideshow-line:before {content: "\f0ac";}.ri-smartphone-fill:before {content: "\f0ad";}.ri-smartphone-line:before {content: "\f0ae";}.ri-snapchat-fill:before {content: "\f0af";}.ri-snapchat-line:before {content: "\f0b0";}.ri-snowy-fill:before {content: "\f0b1";}.ri-snowy-line:before {content: "\f0b2";}.ri-sound-module-fill:before {content: "\f0b3";}.ri-sound-module-line:before {content: "\f0b4";}.ri-soundcloud-fill:before {content: "\f0b5";}.ri-soundcloud-line:before {content: "\f0b6";}.ri-space-ship-fill:before {content: "\f0b7";}.ri-space-ship-line:before {content: "\f0b8";}.ri-space:before {content: "\f0b9";}.ri-spam-2-fill:before {content: "\f0ba";}.ri-spam-2-line:before {content: "\f0bb";}.ri-spam-3-fill:before {content: "\f0bc";}.ri-spam-3-line:before {content: "\f0bd";}.ri-spam-fill:before {content: "\f0be";}.ri-spam-line:before {content: "\f0bf";}.ri-speaker-2-fill:before {content: "\f0c0";}.ri-speaker-2-line:before {content: "\f0c1";}.ri-speaker-3-fill:before {content: "\f0c2";}.ri-speaker-3-line:before {content: "\f0c3";}.ri-speaker-fill:before {content: "\f0c4";}.ri-speaker-line:before {content: "\f0c5";}.ri-spectrum-fill:before {content: "\f0c6";}.ri-spectrum-line:before {content: "\f0c7";}.ri-speed-fill:before {content: "\f0c8";}.ri-speed-line:before {content: "\f0c9";}.ri-speed-mini-fill:before {content: "\f0ca";}.ri-speed-mini-line:before {content: "\f0cb";}.ri-spotify-fill:before {content: "\f0cc";}.ri-spotify-line:before {content: "\f0cd";}.ri-spy-fill:before {content: "\f0ce";}.ri-spy-line:before {content: "\f0cf";}.ri-stack-fill:before {content: "\f0d0";}.ri-stack-line:before {content: "\f0d1";}.ri-stack-overflow-fill:before {content: "\f0d2";}.ri-stack-overflow-line:before {content: "\f0d3";}.ri-stackshare-fill:before {content: "\f0d4";}.ri-stackshare-line:before {content: "\f0d5";}.ri-star-fill:before {content: "\f0d6";}.ri-star-half-fill:before {content: "\f0d7";}.ri-star-half-line:before {content: "\f0d8";}.ri-star-half-s-fill:before {content: "\f0d9";}.ri-star-half-s-line:before {content: "\f0da";}.ri-star-line:before {content: "\f0db";}.ri-star-s-fill:before {content: "\f0dc";}.ri-star-s-line:before {content: "\f0dd";}.ri-star-smile-fill:before {content: "\f0de";}.ri-star-smile-line:before {content: "\f0df";}.ri-steering-2-fill:before {content: "\f0e0";}.ri-steering-2-line:before {content: "\f0e1";}.ri-steering-fill:before {content: "\f0e2";}.ri-steering-line:before {content: "\f0e3";}.ri-sticky-note-2-fill:before {content: "\f0e4";}.ri-sticky-note-2-line:before {content: "\f0e5";}.ri-sticky-note-fill:before {content: "\f0e6";}.ri-sticky-note-line:before {content: "\f0e7";}.ri-stock-fill:before {content: "\f0e8";}.ri-stock-line:before {content: "\f0e9";}.ri-stop-circle-fill:before {content: "\f0ea";}.ri-stop-circle-line:before {content: "\f0eb";}.ri-stop-fill:before {content: "\f0ec";}.ri-stop-line:before {content: "\f0ed";}.ri-stop-mini-fill:before {content: "\f0ee";}.ri-stop-mini-line:before {content: "\f0ef";}.ri-store-2-fill:before {content: "\f0f0";}.ri-store-2-line:before {content: "\f0f1";}.ri-store-3-fill:before {content: "\f0f2";}.ri-store-3-line:before {content: "\f0f3";}.ri-store-fill:before {content: "\f0f4";}.ri-store-line:before {content: "\f0f5";}.ri-strikethrough-2:before {content: "\f0f6";}.ri-strikethrough:before {content: "\f0f7";}.ri-subscript-2:before {content: "\f0f8";}.ri-subscript:before {content: "\f0f9";}.ri-subtract-fill:before {content: "\f0fa";}.ri-subtract-line:before {content: "\f0fb";}.ri-subway-fill:before {content: "\f0fc";}.ri-subway-line:before {content: "\f0fd";}.ri-subway-wifi-fill:before {content: "\f0fe";}.ri-subway-wifi-line:before {content: "\f0ff";}.ri-sun-cloudy-fill:before {content: "\f100";}.ri-sun-cloudy-line:before {content: "\f101";}.ri-sun-fill:before {content: "\f102";}.ri-sun-foggy-fill:before {content: "\f103";}.ri-sun-foggy-line:before {content: "\f104";}.ri-sun-line:before {content: "\f105";}.ri-superscript-2:before {content: "\f106";}.ri-superscript:before {content: "\f107";}.ri-surround-sound-fill:before {content: "\f108";}.ri-surround-sound-line:before {content: "\f109";}.ri-swap-box-fill:before {content: "\f10a";}.ri-swap-box-line:before {content: "\f10b";}.ri-swap-fill:before {content: "\f10c";}.ri-swap-line:before {content: "\f10d";}.ri-switch-fill:before {content: "\f10e";}.ri-switch-line:before {content: "\f10f";}.ri-sword-fill:before {content: "\f110";}.ri-sword-line:before {content: "\f111";}.ri-t-box-fill:before {content: "\f112";}.ri-t-box-line:before {content: "\f113";}.ri-t-shirt-2-fill:before {content: "\f114";}.ri-t-shirt-2-line:before {content: "\f115";}.ri-t-shirt-air-fill:before {content: "\f116";}.ri-t-shirt-air-line:before {content: "\f117";}.ri-t-shirt-fill:before {content: "\f118";}.ri-t-shirt-line:before {content: "\f119";}.ri-table-2:before {content: "\f11a";}.ri-table-alt-fill:before {content: "\f11b";}.ri-table-alt-line:before {content: "\f11c";}.ri-table-fill:before {content: "\f11d";}.ri-table-line:before {content: "\f11e";}.ri-tablet-fill:before {content: "\f11f";}.ri-tablet-line:before {content: "\f120";}.ri-takeaway-fill:before {content: "\f121";}.ri-takeaway-line:before {content: "\f122";}.ri-taobao-fill:before {content: "\f123";}.ri-taobao-line:before {content: "\f124";}.ri-tape-fill:before {content: "\f125";}.ri-tape-line:before {content: "\f126";}.ri-task-fill:before {content: "\f127";}.ri-task-line:before {content: "\f128";}.ri-taxi-fill:before {content: "\f129";}.ri-taxi-line:before {content: "\f12a";}.ri-taxi-wifi-fill:before {content: "\f12b";}.ri-taxi-wifi-line:before {content: "\f12c";}.ri-team-fill:before {content: "\f12d";}.ri-team-line:before {content: "\f12e";}.ri-telegram-fill:before {content: "\f12f";}.ri-telegram-line:before {content: "\f130";}.ri-temp-cold-fill:before {content: "\f131";}.ri-temp-cold-line:before {content: "\f132";}.ri-temp-hot-fill:before {content: "\f133";}.ri-temp-hot-line:before {content: "\f134";}.ri-terminal-box-fill:before {content: "\f135";}.ri-terminal-box-line:before {content: "\f136";}.ri-terminal-fill:before {content: "\f137";}.ri-terminal-line:before {content: "\f138";}.ri-terminal-window-fill:before {content: "\f139";}.ri-terminal-window-line:before {content: "\f13a";}.ri-text-direction-l:before {content: "\f13b";}.ri-text-direction-r:before {content: "\f13c";}.ri-text-spacing:before {content: "\f13d";}.ri-text-wrap:before {content: "\f13e";}.ri-text:before {content: "\f13f";}.ri-thumb-down-fill:before {content: "\f140";}.ri-thumb-down-line:before {content: "\f141";}.ri-thumb-up-fill:before {content: "\f142";}.ri-thumb-up-line:before {content: "\f143";}.ri-thunderstorms-fill:before {content: "\f144";}.ri-thunderstorms-line:before {content: "\f145";}.ri-ticket-2-fill:before {content: "\f146";}.ri-ticket-2-line:before {content: "\f147";}.ri-ticket-fill:before {content: "\f148";}.ri-ticket-line:before {content: "\f149";}.ri-time-fill:before {content: "\f14a";}.ri-time-line:before {content: "\f14b";}.ri-timer-2-fill:before {content: "\f14c";}.ri-timer-2-line:before {content: "\f14d";}.ri-timer-fill:before {content: "\f14e";}.ri-timer-flash-fill:before {content: "\f14f";}.ri-timer-flash-line:before {content: "\f150";}.ri-timer-line:before {content: "\f151";}.ri-todo-fill:before {content: "\f152";}.ri-todo-line:before {content: "\f153";}.ri-toggle-fill:before {content: "\f154";}.ri-toggle-line:before {content: "\f155";}.ri-tools-fill:before {content: "\f156";}.ri-tools-line:before {content: "\f157";}.ri-tornado-fill:before {content: "\f158";}.ri-tornado-line:before {content: "\f159";}.ri-trademark-fill:before {content: "\f15a";}.ri-trademark-line:before {content: "\f15b";}.ri-traffic-light-fill:before {content: "\f15c";}.ri-traffic-light-line:before {content: "\f15d";}.ri-train-fill:before {content: "\f15e";}.ri-train-line:before {content: "\f15f";}.ri-train-wifi-fill:before {content: "\f160";}.ri-train-wifi-line:before {content: "\f161";}.ri-translate-2:before {content: "\f162";}.ri-translate:before {content: "\f163";}.ri-travesti-fill:before {content: "\f164";}.ri-travesti-line:before {content: "\f165";}.ri-treasure-map-fill:before {content: "\f166";}.ri-treasure-map-line:before {content: "\f167";}.ri-trello-fill:before {content: "\f168";}.ri-trello-line:before {content: "\f169";}.ri-trophy-fill:before {content: "\f16a";}.ri-trophy-line:before {content: "\f16b";}.ri-truck-fill:before {content: "\f16c";}.ri-truck-line:before {content: "\f16d";}.ri-tumblr-fill:before {content: "\f16e";}.ri-tumblr-line:before {content: "\f16f";}.ri-tv-2-fill:before {content: "\f170";}.ri-tv-2-line:before {content: "\f171";}.ri-tv-fill:before {content: "\f172";}.ri-tv-line:before {content: "\f173";}.ri-twitch-fill:before {content: "\f174";}.ri-twitch-line:before {content: "\f175";}.ri-twitter-fill:before {content: "\f176";}.ri-twitter-line:before {content: "\f177";}.ri-typhoon-fill:before {content: "\f178";}.ri-typhoon-line:before {content: "\f179";}.ri-u-disk-fill:before {content: "\f17a";}.ri-u-disk-line:before {content: "\f17b";}.ri-ubuntu-fill:before {content: "\f17c";}.ri-ubuntu-line:before {content: "\f17d";}.ri-umbrella-fill:before {content: "\f17e";}.ri-umbrella-line:before {content: "\f17f";}.ri-underline:before {content: "\f180";}.ri-uninstall-fill:before {content: "\f181";}.ri-uninstall-line:before {content: "\f182";}.ri-upload-2-fill:before {content: "\f183";}.ri-upload-2-line:before {content: "\f184";}.ri-upload-cloud-2-fill:before {content: "\f185";}.ri-upload-cloud-2-line:before {content: "\f186";}.ri-upload-cloud-fill:before {content: "\f187";}.ri-upload-cloud-line:before {content: "\f188";}.ri-upload-fill:before {content: "\f189";}.ri-upload-line:before {content: "\f18a";}.ri-user-2-fill:before {content: "\f18b";}.ri-user-2-line:before {content: "\f18c";}.ri-user-3-fill:before {content: "\f18d";}.ri-user-3-line:before {content: "\f18e";}.ri-user-4-fill:before {content: "\f18f";}.ri-user-4-line:before {content: "\f190";}.ri-user-5-fill:before {content: "\f191";}.ri-user-5-line:before {content: "\f192";}.ri-user-6-fill:before {content: "\f193";}.ri-user-6-line:before {content: "\f194";}.ri-user-add-fill:before {content: "\f195";}.ri-user-add-line:before {content: "\f196";}.ri-user-fill:before {content: "\f197";}.ri-user-follow-fill:before {content: "\f198";}.ri-user-follow-line:before {content: "\f199";}.ri-user-heart-fill:before {content: "\f19a";}.ri-user-heart-line:before {content: "\f19b";}.ri-user-line:before {content: "\f19c";}.ri-user-location-fill:before {content: "\f19d";}.ri-user-location-line:before {content: "\f19e";}.ri-user-received-2-fill:before {content: "\f19f";}.ri-user-received-2-line:before {content: "\f1a0";}.ri-user-received-fill:before {content: "\f1a1";}.ri-user-received-line:before {content: "\f1a2";}.ri-user-search-fill:before {content: "\f1a3";}.ri-user-search-line:before {content: "\f1a4";}.ri-user-settings-fill:before {content: "\f1a5";}.ri-user-settings-line:before {content: "\f1a6";}.ri-user-shared-2-fill:before {content: "\f1a7";}.ri-user-shared-2-line:before {content: "\f1a8";}.ri-user-shared-fill:before {content: "\f1a9";}.ri-user-shared-line:before {content: "\f1aa";}.ri-user-smile-fill:before {content: "\f1ab";}.ri-user-smile-line:before {content: "\f1ac";}.ri-user-star-fill:before {content: "\f1ad";}.ri-user-star-line:before {content: "\f1ae";}.ri-user-unfollow-fill:before {content: "\f1af";}.ri-user-unfollow-line:before {content: "\f1b0";}.ri-user-voice-fill:before {content: "\f1b1";}.ri-user-voice-line:before {content: "\f1b2";}.ri-video-chat-fill:before {content: "\f1b3";}.ri-video-chat-line:before {content: "\f1b4";}.ri-video-fill:before {content: "\f1b5";}.ri-video-line:before {content: "\f1b6";}.ri-vidicon-2-fill:before {content: "\f1b7";}.ri-vidicon-2-line:before {content: "\f1b8";}.ri-vidicon-fill:before {content: "\f1b9";}.ri-vidicon-line:before {content: "\f1ba";}.ri-vip-crown-2-fill:before {content: "\f1bb";}.ri-vip-crown-2-line:before {content: "\f1bc";}.ri-vip-crown-fill:before {content: "\f1bd";}.ri-vip-crown-line:before {content: "\f1be";}.ri-vip-diamond-fill:before {content: "\f1bf";}.ri-vip-diamond-line:before {content: "\f1c0";}.ri-vip-fill:before {content: "\f1c1";}.ri-vip-line:before {content: "\f1c2";}.ri-visa-fill:before {content: "\f1c3";}.ri-visa-line:before {content: "\f1c4";}.ri-voice-recognition-fill:before {content: "\f1c5";}.ri-voice-recognition-line:before {content: "\f1c6";}.ri-voiceprint-fill:before {content: "\f1c7";}.ri-voiceprint-line:before {content: "\f1c8";}.ri-volume-down-fill:before {content: "\f1c9";}.ri-volume-down-line:before {content: "\f1ca";}.ri-volume-mute-fill:before {content: "\f1cb";}.ri-volume-mute-line:before {content: "\f1cc";}.ri-volume-off-vibrate-fill:before {content: "\f1cd";}.ri-volume-off-vibrate-line:before {content: "\f1ce";}.ri-volume-up-fill:before {content: "\f1cf";}.ri-volume-up-line:before {content: "\f1d0";}.ri-volume-vibrate-fill:before {content: "\f1d1";}.ri-volume-vibrate-line:before {content: "\f1d2";}.ri-vuejs-fill:before {content: "\f1d3";}.ri-vuejs-line:before {content: "\f1d4";}.ri-walk-fill:before {content: "\f1d5";}.ri-walk-line:before {content: "\f1d6";}.ri-wallet-2-fill:before {content: "\f1d7";}.ri-wallet-2-line:before {content: "\f1d8";}.ri-wallet-3-fill:before {content: "\f1d9";}.ri-wallet-3-line:before {content: "\f1da";}.ri-wallet-fill:before {content: "\f1db";}.ri-wallet-line:before {content: "\f1dc";}.ri-water-flash-fill:before {content: "\f1dd";}.ri-water-flash-line:before {content: "\f1de";}.ri-webcam-fill:before {content: "\f1df";}.ri-webcam-line:before {content: "\f1e0";}.ri-wechat-2-fill:before {content: "\f1e1";}.ri-wechat-2-line:before {content: "\f1e2";}.ri-wechat-fill:before {content: "\f1e3";}.ri-wechat-line:before {content: "\f1e4";}.ri-wechat-pay-fill:before {content: "\f1e5";}.ri-wechat-pay-line:before {content: "\f1e6";}.ri-weibo-fill:before {content: "\f1e7";}.ri-weibo-line:before {content: "\f1e8";}.ri-whatsapp-fill:before {content: "\f1e9";}.ri-whatsapp-line:before {content: "\f1ea";}.ri-wifi-fill:before {content: "\f1eb";}.ri-wifi-line:before {content: "\f1ec";}.ri-wifi-off-fill:before {content: "\f1ed";}.ri-wifi-off-line:before {content: "\f1ee";}.ri-window-2-fill:before {content: "\f1ef";}.ri-window-2-line:before {content: "\f1f0";}.ri-window-fill:before {content: "\f1f1";}.ri-window-line:before {content: "\f1f2";}.ri-windows-fill:before {content: "\f1f3";}.ri-windows-line:before {content: "\f1f4";}.ri-windy-fill:before {content: "\f1f5";}.ri-windy-line:before {content: "\f1f6";}.ri-women-fill:before {content: "\f1f7";}.ri-women-line:before {content: "\f1f8";}.ri-wubi-input:before {content: "\f1f9";}.ri-xbox-fill:before {content: "\f1fa";}.ri-xbox-line:before {content: "\f1fb";}.ri-xing-fill:before {content: "\f1fc";}.ri-xing-line:before {content: "\f1fd";}.ri-youtube-fill:before {content: "\f1fe";}.ri-youtube-line:before {content: "\f1ff";}.ri-zcool-fill:before {content: "\f200";}.ri-zcool-line:before {content: "\f201";}.ri-zhihu-fill:before {content: "\f202";}.ri-zhihu-line:before {content: "\f203";}.ri-zoom-in-fill:before {content: "\f204";}.ri-zoom-in-line:before {content: "\f205";}.ri-zoom-out-fill:before {content: "\f206";}.ri-zoom-out-line:before {content: "\f207";}
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */@font-face{font-family:'FontAwesome';src:url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.eot?v=4.7.0');src:url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'),url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'),url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'),url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'),url('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');font-weight:normal;font-style:normal}.fa{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.fa-lg{font-size:1.33333333em;line-height:.75em;vertical-align:-15%}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-fw{width:1.28571429em;text-align:center}.fa-ul{padding-left:0;margin-left:2.14285714em;list-style-type:none}.fa-ul>li{position:relative}.fa-li{position:absolute;left:-2.14285714em;width:2.14285714em;top:.14285714em;text-align:center}.fa-li.fa-lg{left:-1.85714286em}.fa-border{padding:.2em .25em .15em;border:solid .08em #eee;border-radius:.1em}.fa-pull-left{float:left}.fa-pull-right{float:right}.fa.fa-pull-left{margin-right:.3em}.fa.fa-pull-right{margin-left:.3em}.pull-right{float:right}.pull-left{float:left}.fa.pull-left{margin-right:.3em}.fa.pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s infinite linear;animation:fa-spin 2s infinite linear}.fa-pulse{-webkit-animation:fa-spin 1s infinite steps(8);animation:fa-spin 1s infinite steps(8)}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}.fa-rotate-90{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";-webkit-transform:rotate(90deg);-ms-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";-webkit-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";-webkit-transform:rotate(270deg);-ms-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";-webkit-transform:scale(-1, 1);-ms-transform:scale(-1, 1);transform:scale(-1, 1)}.fa-flip-vertical{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";-webkit-transform:scale(1, -1);-ms-transform:scale(1, -1);transform:scale(1, -1)}:root .fa-rotate-90,:root .fa-rotate-180,:root .fa-rotate-270,:root .fa-flip-horizontal,:root .fa-flip-vertical{filter:none}.fa-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:middle}.fa-stack-1x,.fa-stack-2x{position:absolute;left:0;width:100%;text-align:center}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:#fff}.fa-glass:before{content:"\f000"}.fa-music:before{content:"\f001"}.fa-search:before{content:"\f002"}.fa-envelope-o:before{content:"\f003"}.fa-heart:before{content:"\f004"}.fa-star:before{content:"\f005"}.fa-star-o:before{content:"\f006"}.fa-user:before{content:"\f007"}.fa-film:before{content:"\f008"}.fa-th-large:before{content:"\f009"}.fa-th:before{content:"\f00a"}.fa-th-list:before{content:"\f00b"}.fa-check:before{content:"\f00c"}.fa-remove:before,.fa-close:before,.fa-times:before{content:"\f00d"}.fa-search-plus:before{content:"\f00e"}.fa-search-minus:before{content:"\f010"}.fa-power-off:before{content:"\f011"}.fa-signal:before{content:"\f012"}.fa-gear:before,.fa-cog:before{content:"\f013"}.fa-trash-o:before{content:"\f014"}.fa-home:before{content:"\f015"}.fa-file-o:before{content:"\f016"}.fa-clock-o:before{content:"\f017"}.fa-road:before{content:"\f018"}.fa-download:before{content:"\f019"}.fa-arrow-circle-o-down:before{content:"\f01a"}.fa-arrow-circle-o-up:before{content:"\f01b"}.fa-inbox:before{content:"\f01c"}.fa-play-circle-o:before{content:"\f01d"}.fa-rotate-right:before,.fa-repeat:before{content:"\f01e"}.fa-refresh:before{content:"\f021"}.fa-list-alt:before{content:"\f022"}.fa-lock:before{content:"\f023"}.fa-flag:before{content:"\f024"}.fa-headphones:before{content:"\f025"}.fa-volume-off:before{content:"\f026"}.fa-volume-down:before{content:"\f027"}.fa-volume-up:before{content:"\f028"}.fa-qrcode:before{content:"\f029"}.fa-barcode:before{content:"\f02a"}.fa-tag:before{content:"\f02b"}.fa-tags:before{content:"\f02c"}.fa-book:before{content:"\f02d"}.fa-bookmark:before{content:"\f02e"}.fa-print:before{content:"\f02f"}.fa-camera:before{content:"\f030"}.fa-font:before{content:"\f031"}.fa-bold:before{content:"\f032"}.fa-italic:before{content:"\f033"}.fa-text-height:before{content:"\f034"}.fa-text-width:before{content:"\f035"}.fa-align-left:before{content:"\f036"}.fa-align-center:before{content:"\f037"}.fa-align-right:before{content:"\f038"}.fa-align-justify:before{content:"\f039"}.fa-list:before{content:"\f03a"}.fa-dedent:before,.fa-outdent:before{content:"\f03b"}.fa-indent:before{content:"\f03c"}.fa-video-camera:before{content:"\f03d"}.fa-photo:before,.fa-image:before,.fa-picture-o:before{content:"\f03e"}.fa-pencil:before{content:"\f040"}.fa-map-marker:before{content:"\f041"}.fa-adjust:before{content:"\f042"}.fa-tint:before{content:"\f043"}.fa-edit:before,.fa-pencil-square-o:before{content:"\f044"}.fa-share-square-o:before{content:"\f045"}.fa-check-square-o:before{content:"\f046"}.fa-arrows:before{content:"\f047"}.fa-step-backward:before{content:"\f048"}.fa-fast-backward:before{content:"\f049"}.fa-backward:before{content:"\f04a"}.fa-play:before{content:"\f04b"}.fa-pause:before{content:"\f04c"}.fa-stop:before{content:"\f04d"}.fa-forward:before{content:"\f04e"}.fa-fast-forward:before{content:"\f050"}.fa-step-forward:before{content:"\f051"}.fa-eject:before{content:"\f052"}.fa-chevron-left:before{content:"\f053"}.fa-chevron-right:before{content:"\f054"}.fa-plus-circle:before{content:"\f055"}.fa-minus-circle:before{content:"\f056"}.fa-times-circle:before{content:"\f057"}.fa-check-circle:before{content:"\f058"}.fa-question-circle:before{content:"\f059"}.fa-info-circle:before{content:"\f05a"}.fa-crosshairs:before{content:"\f05b"}.fa-times-circle-o:before{content:"\f05c"}.fa-check-circle-o:before{content:"\f05d"}.fa-ban:before{content:"\f05e"}.fa-arrow-left:before{content:"\f060"}.fa-arrow-right:before{content:"\f061"}.fa-arrow-up:before{content:"\f062"}.fa-arrow-down:before{content:"\f063"}.fa-mail-forward:before,.fa-share:before{content:"\f064"}.fa-expand:before{content:"\f065"}.fa-compress:before{content:"\f066"}.fa-plus:before{content:"\f067"}.fa-minus:before{content:"\f068"}.fa-asterisk:before{content:"\f069"}.fa-exclamation-circle:before{content:"\f06a"}.fa-gift:before{content:"\f06b"}.fa-leaf:before{content:"\f06c"}.fa-fire:before{content:"\f06d"}.fa-eye:before{content:"\f06e"}.fa-eye-slash:before{content:"\f070"}.fa-warning:before,.fa-exclamation-triangle:before{content:"\f071"}.fa-plane:before{content:"\f072"}.fa-calendar:before{content:"\f073"}.fa-random:before{content:"\f074"}.fa-comment:before{content:"\f075"}.fa-magnet:before{content:"\f076"}.fa-chevron-up:before{content:"\f077"}.fa-chevron-down:before{content:"\f078"}.fa-retweet:before{content:"\f079"}.fa-shopping-cart:before{content:"\f07a"}.fa-folder:before{content:"\f07b"}.fa-folder-open:before{content:"\f07c"}.fa-arrows-v:before{content:"\f07d"}.fa-arrows-h:before{content:"\f07e"}.fa-bar-chart-o:before,.fa-bar-chart:before{content:"\f080"}.fa-twitter-square:before{content:"\f081"}.fa-facebook-square:before{content:"\f082"}.fa-camera-retro:before{content:"\f083"}.fa-key:before{content:"\f084"}.fa-gears:before,.fa-cogs:before{content:"\f085"}.fa-comments:before{content:"\f086"}.fa-thumbs-o-up:before{content:"\f087"}.fa-thumbs-o-down:before{content:"\f088"}.fa-star-half:before{content:"\f089"}.fa-heart-o:before{content:"\f08a"}.fa-sign-out:before{content:"\f08b"}.fa-linkedin-square:before{content:"\f08c"}.fa-thumb-tack:before{content:"\f08d"}.fa-external-link:before{content:"\f08e"}.fa-sign-in:before{content:"\f090"}.fa-trophy:before{content:"\f091"}.fa-github-square:before{content:"\f092"}.fa-upload:before{content:"\f093"}.fa-lemon-o:before{content:"\f094"}.fa-phone:before{content:"\f095"}.fa-square-o:before{content:"\f096"}.fa-bookmark-o:before{content:"\f097"}.fa-phone-square:before{content:"\f098"}.fa-twitter:before{content:"\f099"}.fa-facebook-f:before,.fa-facebook:before{content:"\f09a"}.fa-github:before{content:"\f09b"}.fa-unlock:before{content:"\f09c"}.fa-credit-card:before{content:"\f09d"}.fa-feed:before,.fa-rss:before{content:"\f09e"}.fa-hdd-o:before{content:"\f0a0"}.fa-bullhorn:before{content:"\f0a1"}.fa-bell:before{content:"\f0f3"}.fa-certificate:before{content:"\f0a3"}.fa-hand-o-right:before{content:"\f0a4"}.fa-hand-o-left:before{content:"\f0a5"}.fa-hand-o-up:before{content:"\f0a6"}.fa-hand-o-down:before{content:"\f0a7"}.fa-arrow-circle-left:before{content:"\f0a8"}.fa-arrow-circle-right:before{content:"\f0a9"}.fa-arrow-circle-up:before{content:"\f0aa"}.fa-arrow-circle-down:before{content:"\f0ab"}.fa-globe:before{content:"\f0ac"}.fa-wrench:before{content:"\f0ad"}.fa-tasks:before{content:"\f0ae"}.fa-filter:before{content:"\f0b0"}.fa-briefcase:before{content:"\f0b1"}.fa-arrows-alt:before{content:"\f0b2"}.fa-group:before,.fa-users:before{content:"\f0c0"}.fa-chain:before,.fa-link:before{content:"\f0c1"}.fa-cloud:before{content:"\f0c2"}.fa-flask:before{content:"\f0c3"}.fa-cut:before,.fa-scissors:before{content:"\f0c4"}.fa-copy:before,.fa-files-o:before{content:"\f0c5"}.fa-paperclip:before{content:"\f0c6"}.fa-save:before,.fa-floppy-o:before{content:"\f0c7"}.fa-square:before{content:"\f0c8"}.fa-navicon:before,.fa-reorder:before,.fa-bars:before{content:"\f0c9"}.fa-list-ul:before{content:"\f0ca"}.fa-list-ol:before{content:"\f0cb"}.fa-strikethrough:before{content:"\f0cc"}.fa-underline:before{content:"\f0cd"}.fa-table:before{content:"\f0ce"}.fa-magic:before{content:"\f0d0"}.fa-truck:before{content:"\f0d1"}.fa-pinterest:before{content:"\f0d2"}.fa-pinterest-square:before{content:"\f0d3"}.fa-google-plus-square:before{content:"\f0d4"}.fa-google-plus:before{content:"\f0d5"}.fa-money:before{content:"\f0d6"}.fa-caret-down:before{content:"\f0d7"}.fa-caret-up:before{content:"\f0d8"}.fa-caret-left:before{content:"\f0d9"}.fa-caret-right:before{content:"\f0da"}.fa-columns:before{content:"\f0db"}.fa-unsorted:before,.fa-sort:before{content:"\f0dc"}.fa-sort-down:before,.fa-sort-desc:before{content:"\f0dd"}.fa-sort-up:before,.fa-sort-asc:before{content:"\f0de"}.fa-envelope:before{content:"\f0e0"}.fa-linkedin:before{content:"\f0e1"}.fa-rotate-left:before,.fa-undo:before{content:"\f0e2"}.fa-legal:before,.fa-gavel:before{content:"\f0e3"}.fa-dashboard:before,.fa-tachometer:before{content:"\f0e4"}.fa-comment-o:before{content:"\f0e5"}.fa-comments-o:before{content:"\f0e6"}.fa-flash:before,.fa-bolt:before{content:"\f0e7"}.fa-sitemap:before{content:"\f0e8"}.fa-umbrella:before{content:"\f0e9"}.fa-paste:before,.fa-clipboard:before{content:"\f0ea"}.fa-lightbulb-o:before{content:"\f0eb"}.fa-exchange:before{content:"\f0ec"}.fa-cloud-download:before{content:"\f0ed"}.fa-cloud-upload:before{content:"\f0ee"}.fa-user-md:before{content:"\f0f0"}.fa-stethoscope:before{content:"\f0f1"}.fa-suitcase:before{content:"\f0f2"}.fa-bell-o:before{content:"\f0a2"}.fa-coffee:before{content:"\f0f4"}.fa-cutlery:before{content:"\f0f5"}.fa-file-text-o:before{content:"\f0f6"}.fa-building-o:before{content:"\f0f7"}.fa-hospital-o:before{content:"\f0f8"}.fa-ambulance:before{content:"\f0f9"}.fa-medkit:before{content:"\f0fa"}.fa-fighter-jet:before{content:"\f0fb"}.fa-beer:before{content:"\f0fc"}.fa-h-square:before{content:"\f0fd"}.fa-plus-square:before{content:"\f0fe"}.fa-angle-double-left:before{content:"\f100"}.fa-angle-double-right:before{content:"\f101"}.fa-angle-double-up:before{content:"\f102"}.fa-angle-double-down:before{content:"\f103"}.fa-angle-left:before{content:"\f104"}.fa-angle-right:before{content:"\f105"}.fa-angle-up:before{content:"\f106"}.fa-angle-down:before{content:"\f107"}.fa-desktop:before{content:"\f108"}.fa-laptop:before{content:"\f109"}.fa-tablet:before{content:"\f10a"}.fa-mobile-phone:before,.fa-mobile:before{content:"\f10b"}.fa-circle-o:before{content:"\f10c"}.fa-quote-left:before{content:"\f10d"}.fa-quote-right:before{content:"\f10e"}.fa-spinner:before{content:"\f110"}.fa-circle:before{content:"\f111"}.fa-mail-reply:before,.fa-reply:before{content:"\f112"}.fa-github-alt:before{content:"\f113"}.fa-folder-o:before{content:"\f114"}.fa-folder-open-o:before{content:"\f115"}.fa-smile-o:before{content:"\f118"}.fa-frown-o:before{content:"\f119"}.fa-meh-o:before{content:"\f11a"}.fa-gamepad:before{content:"\f11b"}.fa-keyboard-o:before{content:"\f11c"}.fa-flag-o:before{content:"\f11d"}.fa-flag-checkered:before{content:"\f11e"}.fa-terminal:before{content:"\f120"}.fa-code:before{content:"\f121"}.fa-mail-reply-all:before,.fa-reply-all:before{content:"\f122"}.fa-star-half-empty:before,.fa-star-half-full:before,.fa-star-half-o:before{content:"\f123"}.fa-location-arrow:before{content:"\f124"}.fa-crop:before{content:"\f125"}.fa-code-fork:before{content:"\f126"}.fa-unlink:before,.fa-chain-broken:before{content:"\f127"}.fa-question:before{content:"\f128"}.fa-info:before{content:"\f129"}.fa-exclamation:before{content:"\f12a"}.fa-superscript:before{content:"\f12b"}.fa-subscript:before{content:"\f12c"}.fa-eraser:before{content:"\f12d"}.fa-puzzle-piece:before{content:"\f12e"}.fa-microphone:before{content:"\f130"}.fa-microphone-slash:before{content:"\f131"}.fa-shield:before{content:"\f132"}.fa-calendar-o:before{content:"\f133"}.fa-fire-extinguisher:before{content:"\f134"}.fa-rocket:before{content:"\f135"}.fa-maxcdn:before{content:"\f136"}.fa-chevron-circle-left:before{content:"\f137"}.fa-chevron-circle-right:before{content:"\f138"}.fa-chevron-circle-up:before{content:"\f139"}.fa-chevron-circle-down:before{content:"\f13a"}.fa-html5:before{content:"\f13b"}.fa-css3:before{content:"\f13c"}.fa-anchor:before{content:"\f13d"}.fa-unlock-alt:before{content:"\f13e"}.fa-bullseye:before{content:"\f140"}.fa-ellipsis-h:before{content:"\f141"}.fa-ellipsis-v:before{content:"\f142"}.fa-rss-square:before{content:"\f143"}.fa-play-circle:before{content:"\f144"}.fa-ticket:before{content:"\f145"}.fa-minus-square:before{content:"\f146"}.fa-minus-square-o:before{content:"\f147"}.fa-level-up:before{content:"\f148"}.fa-level-down:before{content:"\f149"}.fa-check-square:before{content:"\f14a"}.fa-pencil-square:before{content:"\f14b"}.fa-external-link-square:before{content:"\f14c"}.fa-share-square:before{content:"\f14d"}.fa-compass:before{content:"\f14e"}.fa-toggle-down:before,.fa-caret-square-o-down:before{content:"\f150"}.fa-toggle-up:before,.fa-caret-square-o-up:before{content:"\f151"}.fa-toggle-right:before,.fa-caret-square-o-right:before{content:"\f152"}.fa-euro:before,.fa-eur:before{content:"\f153"}.fa-gbp:before{content:"\f154"}.fa-dollar:before,.fa-usd:before{content:"\f155"}.fa-rupee:before,.fa-inr:before{content:"\f156"}.fa-cny:before,.fa-rmb:before,.fa-yen:before,.fa-jpy:before{content:"\f157"}.fa-ruble:before,.fa-rouble:before,.fa-rub:before{content:"\f158"}.fa-won:before,.fa-krw:before{content:"\f159"}.fa-bitcoin:before,.fa-btc:before{content:"\f15a"}.fa-file:before{content:"\f15b"}.fa-file-text:before{content:"\f15c"}.fa-sort-alpha-asc:before{content:"\f15d"}.fa-sort-alpha-desc:before{content:"\f15e"}.fa-sort-amount-asc:before{content:"\f160"}.fa-sort-amount-desc:before{content:"\f161"}.fa-sort-numeric-asc:before{content:"\f162"}.fa-sort-numeric-desc:before{content:"\f163"}.fa-thumbs-up:before{content:"\f164"}.fa-thumbs-down:before{content:"\f165"}.fa-youtube-square:before{content:"\f166"}.fa-youtube:before{content:"\f167"}.fa-xing:before{content:"\f168"}.fa-xing-square:before{content:"\f169"}.fa-youtube-play:before{content:"\f16a"}.fa-dropbox:before{content:"\f16b"}.fa-stack-overflow:before{content:"\f16c"}.fa-instagram:before{content:"\f16d"}.fa-flickr:before{content:"\f16e"}.fa-adn:before{content:"\f170"}.fa-bitbucket:before{content:"\f171"}.fa-bitbucket-square:before{content:"\f172"}.fa-tumblr:before{content:"\f173"}.fa-tumblr-square:before{content:"\f174"}.fa-long-arrow-down:before{content:"\f175"}.fa-long-arrow-up:before{content:"\f176"}.fa-long-arrow-left:before{content:"\f177"}.fa-long-arrow-right:before{content:"\f178"}.fa-apple:before{content:"\f179"}.fa-windows:before{content:"\f17a"}.fa-android:before{content:"\f17b"}.fa-linux:before{content:"\f17c"}.fa-dribbble:before{content:"\f17d"}.fa-skype:before{content:"\f17e"}.fa-foursquare:before{content:"\f180"}.fa-trello:before{content:"\f181"}.fa-female:before{content:"\f182"}.fa-male:before{content:"\f183"}.fa-gittip:before,.fa-gratipay:before{content:"\f184"}.fa-sun-o:before{content:"\f185"}.fa-moon-o:before{content:"\f186"}.fa-archive:before{content:"\f187"}.fa-bug:before{content:"\f188"}.fa-vk:before{content:"\f189"}.fa-weibo:before{content:"\f18a"}.fa-renren:before{content:"\f18b"}.fa-pagelines:before{content:"\f18c"}.fa-stack-exchange:before{content:"\f18d"}.fa-arrow-circle-o-right:before{content:"\f18e"}.fa-arrow-circle-o-left:before{content:"\f190"}.fa-toggle-left:before,.fa-caret-square-o-left:before{content:"\f191"}.fa-dot-circle-o:before{content:"\f192"}.fa-wheelchair:before{content:"\f193"}.fa-vimeo-square:before{content:"\f194"}.fa-turkish-lira:before,.fa-try:before{content:"\f195"}.fa-plus-square-o:before{content:"\f196"}.fa-space-shuttle:before{content:"\f197"}.fa-slack:before{content:"\f198"}.fa-envelope-square:before{content:"\f199"}.fa-wordpress:before{content:"\f19a"}.fa-openid:before{content:"\f19b"}.fa-institution:before,.fa-bank:before,.fa-university:before{content:"\f19c"}.fa-mortar-board:before,.fa-graduation-cap:before{content:"\f19d"}.fa-yahoo:before{content:"\f19e"}.fa-google:before{content:"\f1a0"}.fa-reddit:before{content:"\f1a1"}.fa-reddit-square:before{content:"\f1a2"}.fa-stumbleupon-circle:before{content:"\f1a3"}.fa-stumbleupon:before{content:"\f1a4"}.fa-delicious:before{content:"\f1a5"}.fa-digg:before{content:"\f1a6"}.fa-pied-piper-pp:before{content:"\f1a7"}.fa-pied-piper-alt:before{content:"\f1a8"}.fa-drupal:before{content:"\f1a9"}.fa-joomla:before{content:"\f1aa"}.fa-language:before{content:"\f1ab"}.fa-fax:before{content:"\f1ac"}.fa-building:before{content:"\f1ad"}.fa-child:before{content:"\f1ae"}.fa-paw:before{content:"\f1b0"}.fa-spoon:before{content:"\f1b1"}.fa-cube:before{content:"\f1b2"}.fa-cubes:before{content:"\f1b3"}.fa-behance:before{content:"\f1b4"}.fa-behance-square:before{content:"\f1b5"}.fa-steam:before{content:"\f1b6"}.fa-steam-square:before{content:"\f1b7"}.fa-recycle:before{content:"\f1b8"}.fa-automobile:before,.fa-car:before{content:"\f1b9"}.fa-cab:before,.fa-taxi:before{content:"\f1ba"}.fa-tree:before{content:"\f1bb"}.fa-spotify:before{content:"\f1bc"}.fa-deviantart:before{content:"\f1bd"}.fa-soundcloud:before{content:"\f1be"}.fa-database:before{content:"\f1c0"}.fa-file-pdf-o:before{content:"\f1c1"}.fa-file-word-o:before{content:"\f1c2"}.fa-file-excel-o:before{content:"\f1c3"}.fa-file-powerpoint-o:before{content:"\f1c4"}.fa-file-photo-o:before,.fa-file-picture-o:before,.fa-file-image-o:before{content:"\f1c5"}.fa-file-zip-o:before,.fa-file-archive-o:before{content:"\f1c6"}.fa-file-sound-o:before,.fa-file-audio-o:before{content:"\f1c7"}.fa-file-movie-o:before,.fa-file-video-o:before{content:"\f1c8"}.fa-file-code-o:before{content:"\f1c9"}.fa-vine:before{content:"\f1ca"}.fa-codepen:before{content:"\f1cb"}.fa-jsfiddle:before{content:"\f1cc"}.fa-life-bouy:before,.fa-life-buoy:before,.fa-life-saver:before,.fa-support:before,.fa-life-ring:before{content:"\f1cd"}.fa-circle-o-notch:before{content:"\f1ce"}.fa-ra:before,.fa-resistance:before,.fa-rebel:before{content:"\f1d0"}.fa-ge:before,.fa-empire:before{content:"\f1d1"}.fa-git-square:before{content:"\f1d2"}.fa-git:before{content:"\f1d3"}.fa-y-combinator-square:before,.fa-yc-square:before,.fa-hacker-news:before{content:"\f1d4"}.fa-tencent-weibo:before{content:"\f1d5"}.fa-qq:before{content:"\f1d6"}.fa-wechat:before,.fa-weixin:before{content:"\f1d7"}.fa-send:before,.fa-paper-plane:before{content:"\f1d8"}.fa-send-o:before,.fa-paper-plane-o:before{content:"\f1d9"}.fa-history:before{content:"\f1da"}.fa-circle-thin:before{content:"\f1db"}.fa-header:before{content:"\f1dc"}.fa-paragraph:before{content:"\f1dd"}.fa-sliders:before{content:"\f1de"}.fa-share-alt:before{content:"\f1e0"}.fa-share-alt-square:before{content:"\f1e1"}.fa-bomb:before{content:"\f1e2"}.fa-soccer-ball-o:before,.fa-futbol-o:before{content:"\f1e3"}.fa-tty:before{content:"\f1e4"}.fa-binoculars:before{content:"\f1e5"}.fa-plug:before{content:"\f1e6"}.fa-slideshare:before{content:"\f1e7"}.fa-twitch:before{content:"\f1e8"}.fa-yelp:before{content:"\f1e9"}.fa-newspaper-o:before{content:"\f1ea"}.fa-wifi:before{content:"\f1eb"}.fa-calculator:before{content:"\f1ec"}.fa-paypal:before{content:"\f1ed"}.fa-google-wallet:before{content:"\f1ee"}.fa-cc-visa:before{content:"\f1f0"}.fa-cc-mastercard:before{content:"\f1f1"}.fa-cc-discover:before{content:"\f1f2"}.fa-cc-amex:before{content:"\f1f3"}.fa-cc-paypal:before{content:"\f1f4"}.fa-cc-stripe:before{content:"\f1f5"}.fa-bell-slash:before{content:"\f1f6"}.fa-bell-slash-o:before{content:"\f1f7"}.fa-trash:before{content:"\f1f8"}.fa-copyright:before{content:"\f1f9"}.fa-at:before{content:"\f1fa"}.fa-eyedropper:before{content:"\f1fb"}.fa-paint-brush:before{content:"\f1fc"}.fa-birthday-cake:before{content:"\f1fd"}.fa-area-chart:before{content:"\f1fe"}.fa-pie-chart:before{content:"\f200"}.fa-line-chart:before{content:"\f201"}.fa-lastfm:before{content:"\f202"}.fa-lastfm-square:before{content:"\f203"}.fa-toggle-off:before{content:"\f204"}.fa-toggle-on:before{content:"\f205"}.fa-bicycle:before{content:"\f206"}.fa-bus:before{content:"\f207"}.fa-ioxhost:before{content:"\f208"}.fa-angellist:before{content:"\f209"}.fa-cc:before{content:"\f20a"}.fa-shekel:before,.fa-sheqel:before,.fa-ils:before{content:"\f20b"}.fa-meanpath:before{content:"\f20c"}.fa-buysellads:before{content:"\f20d"}.fa-connectdevelop:before{content:"\f20e"}.fa-dashcube:before{content:"\f210"}.fa-forumbee:before{content:"\f211"}.fa-leanpub:before{content:"\f212"}.fa-sellsy:before{content:"\f213"}.fa-shirtsinbulk:before{content:"\f214"}.fa-simplybuilt:before{content:"\f215"}.fa-skyatlas:before{content:"\f216"}.fa-cart-plus:before{content:"\f217"}.fa-cart-arrow-down:before{content:"\f218"}.fa-diamond:before{content:"\f219"}.fa-ship:before{content:"\f21a"}.fa-user-secret:before{content:"\f21b"}.fa-motorcycle:before{content:"\f21c"}.fa-street-view:before{content:"\f21d"}.fa-heartbeat:before{content:"\f21e"}.fa-venus:before{content:"\f221"}.fa-mars:before{content:"\f222"}.fa-mercury:before{content:"\f223"}.fa-intersex:before,.fa-transgender:before{content:"\f224"}.fa-transgender-alt:before{content:"\f225"}.fa-venus-double:before{content:"\f226"}.fa-mars-double:before{content:"\f227"}.fa-venus-mars:before{content:"\f228"}.fa-mars-stroke:before{content:"\f229"}.fa-mars-stroke-v:before{content:"\f22a"}.fa-mars-stroke-h:before{content:"\f22b"}.fa-neuter:before{content:"\f22c"}.fa-genderless:before{content:"\f22d"}.fa-facebook-official:before{content:"\f230"}.fa-pinterest-p:before{content:"\f231"}.fa-whatsapp:before{content:"\f232"}.fa-server:before{content:"\f233"}.fa-user-plus:before{content:"\f234"}.fa-user-times:before{content:"\f235"}.fa-hotel:before,.fa-bed:before{content:"\f236"}.fa-viacoin:before{content:"\f237"}.fa-train:before{content:"\f238"}.fa-subway:before{content:"\f239"}.fa-medium:before{content:"\f23a"}.fa-yc:before,.fa-y-combinator:before{content:"\f23b"}.fa-optin-monster:before{content:"\f23c"}.fa-opencart:before{content:"\f23d"}.fa-expeditedssl:before{content:"\f23e"}.fa-battery-4:before,.fa-battery:before,.fa-battery-full:before{content:"\f240"}.fa-battery-3:before,.fa-battery-three-quarters:before{content:"\f241"}.fa-battery-2:before,.fa-battery-half:before{content:"\f242"}.fa-battery-1:before,.fa-battery-quarter:before{content:"\f243"}.fa-battery-0:before,.fa-battery-empty:before{content:"\f244"}.fa-mouse-pointer:before{content:"\f245"}.fa-i-cursor:before{content:"\f246"}.fa-object-group:before{content:"\f247"}.fa-object-ungroup:before{content:"\f248"}.fa-sticky-note:before{content:"\f249"}.fa-sticky-note-o:before{content:"\f24a"}.fa-cc-jcb:before{content:"\f24b"}.fa-cc-diners-club:before{content:"\f24c"}.fa-clone:before{content:"\f24d"}.fa-balance-scale:before{content:"\f24e"}.fa-hourglass-o:before{content:"\f250"}.fa-hourglass-1:before,.fa-hourglass-start:before{content:"\f251"}.fa-hourglass-2:before,.fa-hourglass-half:before{content:"\f252"}.fa-hourglass-3:before,.fa-hourglass-end:before{content:"\f253"}.fa-hourglass:before{content:"\f254"}.fa-hand-grab-o:before,.fa-hand-rock-o:before{content:"\f255"}.fa-hand-stop-o:before,.fa-hand-paper-o:before{content:"\f256"}.fa-hand-scissors-o:before{content:"\f257"}.fa-hand-lizard-o:before{content:"\f258"}.fa-hand-spock-o:before{content:"\f259"}.fa-hand-pointer-o:before{content:"\f25a"}.fa-hand-peace-o:before{content:"\f25b"}.fa-trademark:before{content:"\f25c"}.fa-registered:before{content:"\f25d"}.fa-creative-commons:before{content:"\f25e"}.fa-gg:before{content:"\f260"}.fa-gg-circle:before{content:"\f261"}.fa-tripadvisor:before{content:"\f262"}.fa-odnoklassniki:before{content:"\f263"}.fa-odnoklassniki-square:before{content:"\f264"}.fa-get-pocket:before{content:"\f265"}.fa-wikipedia-w:before{content:"\f266"}.fa-safari:before{content:"\f267"}.fa-chrome:before{content:"\f268"}.fa-firefox:before{content:"\f269"}.fa-opera:before{content:"\f26a"}.fa-internet-explorer:before{content:"\f26b"}.fa-tv:before,.fa-television:before{content:"\f26c"}.fa-contao:before{content:"\f26d"}.fa-500px:before{content:"\f26e"}.fa-amazon:before{content:"\f270"}.fa-calendar-plus-o:before{content:"\f271"}.fa-calendar-minus-o:before{content:"\f272"}.fa-calendar-times-o:before{content:"\f273"}.fa-calendar-check-o:before{content:"\f274"}.fa-industry:before{content:"\f275"}.fa-map-pin:before{content:"\f276"}.fa-map-signs:before{content:"\f277"}.fa-map-o:before{content:"\f278"}.fa-map:before{content:"\f279"}.fa-commenting:before{content:"\f27a"}.fa-commenting-o:before{content:"\f27b"}.fa-houzz:before{content:"\f27c"}.fa-vimeo:before{content:"\f27d"}.fa-black-tie:before{content:"\f27e"}.fa-fonticons:before{content:"\f280"}.fa-reddit-alien:before{content:"\f281"}.fa-edge:before{content:"\f282"}.fa-credit-card-alt:before{content:"\f283"}.fa-codiepie:before{content:"\f284"}.fa-modx:before{content:"\f285"}.fa-fort-awesome:before{content:"\f286"}.fa-usb:before{content:"\f287"}.fa-product-hunt:before{content:"\f288"}.fa-mixcloud:before{content:"\f289"}.fa-scribd:before{content:"\f28a"}.fa-pause-circle:before{content:"\f28b"}.fa-pause-circle-o:before{content:"\f28c"}.fa-stop-circle:before{content:"\f28d"}.fa-stop-circle-o:before{content:"\f28e"}.fa-shopping-bag:before{content:"\f290"}.fa-shopping-basket:before{content:"\f291"}.fa-hashtag:before{content:"\f292"}.fa-bluetooth:before{content:"\f293"}.fa-bluetooth-b:before{content:"\f294"}.fa-percent:before{content:"\f295"}.fa-gitlab:before{content:"\f296"}.fa-wpbeginner:before{content:"\f297"}.fa-wpforms:before{content:"\f298"}.fa-envira:before{content:"\f299"}.fa-universal-access:before{content:"\f29a"}.fa-wheelchair-alt:before{content:"\f29b"}.fa-question-circle-o:before{content:"\f29c"}.fa-blind:before{content:"\f29d"}.fa-audio-description:before{content:"\f29e"}.fa-volume-control-phone:before{content:"\f2a0"}.fa-braille:before{content:"\f2a1"}.fa-assistive-listening-systems:before{content:"\f2a2"}.fa-asl-interpreting:before,.fa-american-sign-language-interpreting:before{content:"\f2a3"}.fa-deafness:before,.fa-hard-of-hearing:before,.fa-deaf:before{content:"\f2a4"}.fa-glide:before{content:"\f2a5"}.fa-glide-g:before{content:"\f2a6"}.fa-signing:before,.fa-sign-language:before{content:"\f2a7"}.fa-low-vision:before{content:"\f2a8"}.fa-viadeo:before{content:"\f2a9"}.fa-viadeo-square:before{content:"\f2aa"}.fa-snapchat:before{content:"\f2ab"}.fa-snapchat-ghost:before{content:"\f2ac"}.fa-snapchat-square:before{content:"\f2ad"}.fa-pied-piper:before{content:"\f2ae"}.fa-first-order:before{content:"\f2b0"}.fa-yoast:before{content:"\f2b1"}.fa-themeisle:before{content:"\f2b2"}.fa-google-plus-circle:before,.fa-google-plus-official:before{content:"\f2b3"}.fa-fa:before,.fa-font-awesome:before{content:"\f2b4"}.fa-handshake-o:before{content:"\f2b5"}.fa-envelope-open:before{content:"\f2b6"}.fa-envelope-open-o:before{content:"\f2b7"}.fa-linode:before{content:"\f2b8"}.fa-address-book:before{content:"\f2b9"}.fa-address-book-o:before{content:"\f2ba"}.fa-vcard:before,.fa-address-card:before{content:"\f2bb"}.fa-vcard-o:before,.fa-address-card-o:before{content:"\f2bc"}.fa-user-circle:before{content:"\f2bd"}.fa-user-circle-o:before{content:"\f2be"}.fa-user-o:before{content:"\f2c0"}.fa-id-badge:before{content:"\f2c1"}.fa-drivers-license:before,.fa-id-card:before{content:"\f2c2"}.fa-drivers-license-o:before,.fa-id-card-o:before{content:"\f2c3"}.fa-quora:before{content:"\f2c4"}.fa-free-code-camp:before{content:"\f2c5"}.fa-telegram:before{content:"\f2c6"}.fa-thermometer-4:before,.fa-thermometer:before,.fa-thermometer-full:before{content:"\f2c7"}.fa-thermometer-3:before,.fa-thermometer-three-quarters:before{content:"\f2c8"}.fa-thermometer-2:before,.fa-thermometer-half:before{content:"\f2c9"}.fa-thermometer-1:before,.fa-thermometer-quarter:before{content:"\f2ca"}.fa-thermometer-0:before,.fa-thermometer-empty:before{content:"\f2cb"}.fa-shower:before{content:"\f2cc"}.fa-bathtub:before,.fa-s15:before,.fa-bath:before{content:"\f2cd"}.fa-podcast:before{content:"\f2ce"}.fa-window-maximize:before{content:"\f2d0"}.fa-window-minimize:before{content:"\f2d1"}.fa-window-restore:before{content:"\f2d2"}.fa-times-rectangle:before,.fa-window-close:before{content:"\f2d3"}.fa-times-rectangle-o:before,.fa-window-close-o:before{content:"\f2d4"}.fa-bandcamp:before{content:"\f2d5"}.fa-grav:before{content:"\f2d6"}.fa-etsy:before{content:"\f2d7"}.fa-imdb:before{content:"\f2d8"}.fa-ravelry:before{content:"\f2d9"}.fa-eercast:before{content:"\f2da"}.fa-microchip:before{content:"\f2db"}.fa-snowflake-o:before{content:"\f2dc"}.fa-superpowers:before{content:"\f2dd"}.fa-wpexplorer:before{content:"\f2de"}.fa-meetup:before{content:"\f2e0"}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;margin:0;overflow:visible;clip:auto}

/*-- CSS Variables --*/
:root{
--body-bg:$(body.background);
--body-bg-color:$(body.background.color);
--main-blog-color:$(main.blog.color);
--main-dark-color:$(main.dark.color);
--text-color:$(body.text.color);
--title-color:$(title.color);
--title-hover:$(title.hover);
--menu-bg-color:$(menu.bg);
--menu-color:$(menu.color);
--menu-hover:$(menu.hover);
--top-menu-color:$(top.menu.color);
--footer-bg:$(footer.bg);
--footer-color:$(footer.color);
--footer-hover:$(footer.hover);
}
html.is-dark{
--body-bg:$(body.background);
--body-bg-color:#2b2b2b;
--main-blog-color:#204ecf;
--main-dark-color:#f6f7f8;
--text-color:#b4b6ba;
--title-color:#f6f7f8;
--title-hover:#204ecf;
--menu-bg-color:#202020;
--menu-color:#f6f7f8;
--top-menu-color:#f6f7f8;
--footer-bg:#202020;
--footer-color:#f6f7f8;
}

/*-- Reset CSS --*/
a,abbr,acronym,address,applet,b,big,blockquote,body,caption,center,cite,code,dd,del,dfn,div,dl,dt,em,fieldset,font,form,h1,h2,h3,h4,h5,h6,html,i,iframe,img,ins,kbd,label,legend,li,object,p,pre,q,s,samp,small,span,strike,strong,sub,sup,table,tbody,td,tfoot,th,thead,tr,tt,u,ul,var{
    padding:0;
    border:0;
    outline:0;
    vertical-align:baseline;
    background:0 0;
    text-decoration:none
}
*, :after, :before {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
}
.comments .continue a {
    display: none;
}
form,textarea,input,button{
    -webkit-appearance:none;
    -moz-appearance:none;
    appearance:none;
    border-radius:0
}
dl,ul{
    list-style-position:inside;
    font-weight:400;
    list-style:none
}
ul li{
    list-style:none
}
caption,th{
    text-align:center
}
img{
    border:none;
    position:relative
}
a,a:visited{
    text-decoration:none
}
.clearfix{
    clear:both
}
.section,.widget,.widget ul{
    margin:0;
    padding:0
}
a {
    color:$(body.link.color)
}
a:visited {
color:purple;
}
a img{
    border:0
}
abbr{
    text-decoration:none
}
.CSS_LIGHTBOX{
    z-index:999999!important
}
.CSS_LIGHTBOX{z-index:999999!important}.CSS_LIGHTBOX_ATTRIBUTION_INDEX_CONTAINER .CSS_HCONT_CHILDREN_HOLDER > .CSS_LAYOUT_COMPONENT.CSS_HCONT_CHILD:first-child > .CSS_LAYOUT_COMPONENT{opacity:0}
.separator a{
    clear:none!important;
    float:none!important;
    margin-left:0!important;
    margin-right:0!important
}
#navbar-iframe,.widget-item-control,a.quickedit,.home-link,.feed-links{
    display:none!important
}
.center{
    display:table;
    margin:0 auto;
    position:relative
}
.widget > h2,.widget > h3{
    display:none
}
.flex-content {
    display: flex;
}
.flex-center {
    justify-content: center;
}
/*-- Body Content CSS --*/
 body{
    background:var(--body-bg);
    background-color:var(--body-bg-color);
    font-family:'Barlow', sans-serif;;
    font-size:14px;
    font-weight:400;
    color:var(--text-color);
    word-wrap:break-word;
    margin:0;
    padding:0
}
 #outer-wrapper{
    margin:0; 
    margin-left:300px;
}
 .row{
    width:1170px
}
#overlap-wrapper {
    z-index:100;
}
 #content-wrapper{
    margin:30px auto 40px;
    overflow:hidden;
}
 #content-wrapper > .container{
    margin:0 -15px
}
 #main-wrapper{
    float:left;
    overflow:hidden;
    width:66.66666667%;
    box-sizing:border-box;
    word-wrap:break-word;
    padding:0 15px;
    margin:0
}
 #sidebar-wrapper{
    float:right;
    overflow:hidden;
    width:33.33333333%;
    box-sizing:border-box;
    word-wrap:break-word;
    padding:0 15px
}
.head-ads {
    display: block;
    background: #edcbaf;
}
.heade-ads h2 {
    display: none;
}
.head-ads .widget {
    width: 100%;
    height: auto;
    padding: 0px 0 0px;
    margin: 0 auto;
    text-align: center;
    line-height: 0px;
}
 .post-image-wrap{
    position:relative;
    display:block
}
 .post-image-link,.about-author .avatar-container,.comments .avatar-image-container{
    background-color:rgba(155,155,155,0.07);
    color:transparent!important
}
 .post-thumb{
    display:block;
    position:relative;
    width:100%;
    height:100%;
    object-fit:cover;
    z-index:1;
    opacity: 0;
    transition:opacity .17s ease,transform .17s ease
}
.post-thumb.lazy-yard {
    opacity: 1;
}
 .post-image-link:hover .post-thumb,.post-image-wrap:hover .post-image-link .post-thumb,.hot-item-inner:hover .post-image-link .post-thumb{
    opacity:.9
}
 .post-title{
}
 .post-title a{
    display:block
}
.header-header .flex-left{
    position:relative;
    float:left;
    align-items: center;
    justify-content: space-between;    
    width: 100%;
    max-width: 845px;
}
 .top-bar-nav .widget > .widget-title{
    display:none
}
 .top-bar-nav ul li{
    float:left
}
 .top-bar-nav ul li > a{
    height:65px;
    display:block;
    color:var(--top-menu-color);
    font-size:12px;
    font-weight:500;
    line-height:65px;
    text-transform:uppercase;
    margin:0 10px 0 0;
    padding:0 5px;
    transition:color .17s
}
.top-bar-nav ul li > a i {
    font-size: 16px;
    vertical-align: middle;
    margin-right: 6px;
    position: relative;
    top: -1px;
}
.top-bar-nav ul li:last-child a{
    margin:0;
    padding-right:0;
}
 .top-bar-nav ul > li:hover > a{
    color:$(top.menu.hover)
}
.header-header .flex-right {
     position:relative;
    float:right;
}
 .top-bar-social .widget > .widget-title{
    display:none
}
 .social a:before{
    display:inline-block;
    font-family:FontAwesome;
    font-style:normal;
    font-weight:400
}
 .social .blogger a:before{
    content:"\f37d"
}
 .social .facebook a:before{
    content:"\f09a"
}
 .social .twitter a:before{
    content:"\f099"
}
 .social .gplus a:before{
    content:"\f0d5"
}
 .social .rss a:before{
    content:"\f09e"
}
 .social .youtube a:before{
    content:"\f167"
}
 .social .skype a:before{
    content:"\f17e"
}
 .social .stumbleupon a:before{
    content:"\f1a4"
}
 .social .tumblr a:before{
    content:"\f173"
}
 .social .vk a:before{
    content:"\f189"
}
 .social .stack-overflow a:before{
    content:"\f16c"
}
 .social .github a:before{
    content:"\f09b"
}
 .social .linkedin a:before{
    content:"\f0e1"
}
 .social .dribbble a:before{
    content:"\f17d"
}
 .social .soundcloud a:before{
    content:"\f1be"
}
 .social .behance a:before{
    content:"\f1b4"
}
 .social .digg a:before{
    content:"\f1a6"
}
 .social .instagram a:before{
    content:"\f16d"
}
 .social .pinterest a:before{
    content:"\f0d2"
}
 .social .twitch a:before{
    content:"\f1e8"
}
 .social .delicious a:before{
    content:"\f1a5"
}
 .social .codepen a:before{
    content:"\f1cb"
}
 .social .reddit a:before{
    content:"\f1a1"
}
 .social .whatsapp a:before{
    content:"\f232"
}
 .social .snapchat a:before{
    content:"\f2ac"
}
 .social .email a:before{
    content:"\f0e0"
}
 .social .external-link a:before{
    content:"\f35d"
}
 .social-color .blogger a:hover{
    color:#ff5722
}
 .social-color .facebook a:hover{
    color:#3b5999
}
 .social-color .twitter a:hover{
    color:#00acee
}
 .social-color .gplus a:hover{
    color:#db4a39
}
 .social-color .youtube a:hover{
    color:#f50000
}
 .social-color .instagram a:hover{
    color:#dd277b
}
 .social-color .pinterest a:hover{
    color:#ca2127
}
 .social-color .dribbble a:hover{
    color:#ea4c89
}
 .social-color .linkedin a:hover{
    color:#0077b5
}
 .social-color .tumblr a:hover{
    color:#365069
}
 .social-color .twitch a:hover{
    color:#6441a5
}
 .social-color .rss a:hover{
    color:#ffc200
}
 .social-color .skype a:hover{
    color:#00aff0
}
 .social-color .stumbleupon a:hover{
    color:#eb4823
}
 .social-color .vk a:hover{
    color:#4a76a8
}
 .social-color .stack-overflow a:hover{
    color:#f48024
}
 .social-color .github a:hover{
    color:#24292e
}
 .social-color .soundcloud a:hover{
    background:linear-gradient(#ff7400,#ff3400)
}
 .social-color .behance a:hover{
    color:#191919
}
 .social-color .digg a:hover{
    color:#1b1a19
}
 .social-color .delicious a:hover{
    color:#0076e8
}
 .social-color .codepen a:hover{
    color:#000
}
 .social-color .reddit a:hover{
    color:#ff4500
}
 .social-color .whatsapp a:hover{
    color:#3fbb50
}
 .social-color .snapchat a:hover{
    color:#ffe700
}
 .social-color .email a:hover{
    color:#888
}
 .social-color .external-link a:hover{
    color:var(--main-dark-color)
}
 #header-wrap{
    position:relative;
    margin:0;
    height:65px;
}
 .header-header{
    width:100%;
    position:relative;
    overflow:hidden;
    padding:0;
    text-align:center;
border-bottom:1px solid rgba(155,155,155,0.15);
}
 .header-header .container{
    position:relative;
    margin:0 auto;
    padding:0
}
 .header-logo{
    position:relative;
    width:auto;
text-align:center;
    display: inline-block;
    max-height:60px;
    margin:0;
    padding:0
}
 .header-logo .header-image-wrapper{
    display:block
}
 .header-logo img{
    max-width:100%;
    max-height:60px;
    margin:0
}
.is-dark .header-logo img {
    -webkit-filter: invert(1);
    filter: invert(1);
}
 .header-logo h1{
    color:var(--title-color);
    font-size:35px;
    line-height:1.4em;
    margin:0
}
 .header-logo p{
    font-size:12px;
    margin:5px 0 0
}
 .mobile-menu .main-menu .widget,.mobile-menu .widget > .widget-title{
    display:none
}
.mobile-menu .main-menu .show-menu{
    display:block
}
 .no-posts{
    float:left;
    width:100%;
    height:100px;
    line-height:100px;
    text-align:center
}
.mobile-menu-toggle, .search-menu-toggle{
    display:none;
    width:34px;
    height:65px;
    line-height:65px;
    z-index:20;
    color:var(--main-dark-color);
    font-size:17px;
    font-weight:400;
    text-align:center;
    cursor:pointer;
    transition:color .17s ease
}
 .mobile-menu-toggle:hover, .search-menu-toggle:hover{
    color:var(--menu-hover)
}
 .mobile-menu-toggle:before {
    content:"\f0c9";
  font-family:FontAwesome;
}
 .nav-active .mobile-menu-toggle:before{
    content:"\f00d";
}
.search-menu-toggle:before{
   content: "\f037";
  font-family:remixicon;
}
.mobile-side-menu {
background-color:var(--menu-bg-color);
position: fixed;
    width: 300px;
    height: 100%;
    top: 0;
    left: 0;
    bottom: 0;
    overflow: hidden;
    z-index: 151515;
    left: 0;
    visibility:visible;
    opacity:1;
    box-shadow: 3px 0 7px rgb(0 0 0 / 10%);
    transition: all .25s ease;
}
.slide-menu-header {
    position: relative;
    float: left;
    width: 100%;
    height: 65px;
    background-color: var(--menu-bg-color);
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(155,155,155,0.15);
}
.slide-menu-header .flex-center {
width:100%;
}
 .mobile-logo {
    display:none;
}
 .mobile-logo .logo-content{
    position:relative;
    float:left;
    display:block;
    width:100%;
    height:60px;
    text-align:center;
    z-index:2
}
 .mobile-logo .logo-content > a{
    height:60px;
    display:inline-block;
    padding:10px 0
}
 .mobile-logo .logo-content > a > img{
    max-height:60px
}
 .mobile-logo .logo-content > h3{
    font-size:30px;
    height:60px;
    line-height:60px;
    margin:10px 0 0
}
 .mobile-logo .logo-content > h3 > a{
    color:var(--main-dark-color)
}
.tgl-wrap {
    display: flex;
    height: 65px;
    align-items: center;
    z-index: 20;
    margin: 0;
}
.tgl-wrap .darkmode-toggle {
    width: auto;
    background-color: transparent;
    padding: 0;
    background-color: transparent;
    color: var(--top-menu-color);
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}
.tgl-wrap .darkmode-toggle:after {
    content: 'Dark';
    opacity: 0;
    -webkit-transition: .4s;
    transition: .4s;
    white-space: nowrap;
    position: absolute;
    right: 0;
}
.is-dark .tgl-wrap .darkmode-toggle:after {
    content: 'Light';
}
.tgl-wrap .darkmode-toggle:hover:after{
opacity:.7;
right:-40px
}
.tgl-wrap .darkmode-toggle i {
     display: flex;
    align-items: center;
    width: 50px;
    height: 25px;
    border-radius: 20px;
    border: 1px solid var(--top-menu-color);
    opacity: .8;
    font-style:unset;
}
.tgl-wrap .darkmode-toggle i:before {
    content: "\f102";
    font-weight: 900;
    font-family: remixicon;
    display: block;
    position: relative;
    left: 3px;
    -webkit-transition: .4s;
    transition: .4s;
}
.is-dark .tgl-wrap .darkmode-toggle i:before {
   -webkit-transform: translateX(28px);
    -ms-transform: translateX(28px);
    transform: translateX(28px);
    content: "\eef8";
}
.full-screen-search {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width: 100%;
    text-align: center;
    margin: 0;
    z-index: 15151515;
}
.search-active .full-screen-search {
display:block;
}
.mobile-search{
    flex:1;
    padding:0 15px 0 0
}
 .mobile-search .search-form{
    width:100%;
    height:34px;
    background-color:#e1f5fe;
    overflow:hidden;
    display:flex;
    justify-content:space-between;
    border:0;
    border-radius:8px
}
.is-dark .mobile-search .search-form, .is-dark  .mobile-search .search-form:focus-within {
background:#3a3a3a;
}
 .mobile-search .search-form:focus-within{
    background-color:#e1f5fe;
    box-shadow:0 1px 1px rgba(0,0,0,0.1),0 1px 3px rgba(0,0,0,0.2)
}

 .mobile-search .search-input{
    flex:1;
    width:100%;
    background-color:rgba(0,0,0,0);
    font-family:inherit;
    font-size:14px;
    color:#01579b;
    font-weight:400;
    padding:0 10px;
    border:0;
    outline: none;
}
 .mobile-search .search-input:focus,.mobile-search .search-input::placeholder{
    color:#01579b
}
.is-dark .mobile-search .search-input,  .is-dark .mobile-search .search-input:focus,.is-dark .mobile-search .search-input::placeholder {
color:#f6f7f8;
}
 .mobile-search .search-input::placeholder{
    opacity:.65
}
 .mobile-search .search-action{
    background-color:rgba(0,0,0,0);
    font-family:inherit;
    font-size:12px;
    color:#01579b;
    font-weight:400;
    text-align:center;
    cursor:pointer;
    padding:0 10px;
    border:0;
    opacity:.65
}
.is-dark .mobile-search .search-action {
color:#f6f7f8;
}
 .mobile-search .search-action:before{
    display:block;
    content:'\f002';
    font-family:FontAwesome;
    font-weight:900
}
 .mobile-search .search-action:hover{
    opacity:1
}
 .hide-freepic-pro-mobile-menu{
    display:none;
    height:100%;
    color:var(--menu-color);
    font-size:16px;
    align-items:center;
    cursor:pointer;
    z-index:20;
    padding:0 16px
}
 .hide-freepic-pro-mobile-menu:before{
    content:'\f00d';
    font-family:FontAwesome;
    font-weight:900
}
 .hide-freepic-pro-mobile-menu:hover{
    color:var(--menu-hover)
}
 .overlay, .searchlay{
    display:none;
    visibility: hidden;
    opacity: 0;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(27,27,37,0.6);
    z-index: 151514;
    -webkit-backdrop-filter: saturate(100%) blur(3px);
    -ms-backdrop-filter: saturate(100%) blur(3px);
    -o-backdrop-filter: saturate(100%) blur(3px);
    backdrop-filter: saturate(100%) blur(3px);
    margin: 0;
    transition: all .25s ease;
}
.search-active .searchlay, .nav-active .overlay {
    display:block;
    visibility: visible;
    opacity: 1;
}

.slide-menu-flex{
    position:relative;
    float:left;
    width:100%;
    height:calc(100% - 59px);
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    overflow:hidden;
    overflow-y:auto;
    -webkit-overflow-scrolling:touch;
    margin:0
}
 .mobile-menu-wrap{
     position:relative;
    float:left;
    width:100%;
    background-color:var(--menu-bg-color);
}
 .nav-active .mobile-menu-wrap{
    visibility:visible;
    opacity:1
}
 .mobile-menu{
    position:relative;
    overflow:hidden;
    padding:20px;
    border-top:1px solid rgba(255,255,255,0.03)
}
.main-menu {
    border-bottom: 1px solid rgba(155,155,155,0.15);
    display: flex;
    margin: 0 0 10px;
    padding: 0 0 10px;
}
.side-bar-nav {
    overflow: hidden;
}
.side-bar-nav .widget {
    border-bottom: 1px solid rgba(155,155,155,0.15);
    overflow: hidden;
    margin: 0 0 10px;
    padding: 0 0 10px;
}
.side-bar-nav .widget:last-child {
    border: 0;
}
 .mobile-menu > ul{
    margin:0
}
 .mobile-menu .m-sub{
    display:none;
    padding:0
}
.mobile-menu ul li ul.m-sub {
    padding-left: 15px;
    box-sizing: border-box;
}
 .mobile-menu ul li{
    position:relative;
    display:block;
    overflow:hidden;
    float:left;
    width:100%;
    font-size:14px;
    line-height:38px
}
 .mobile-menu > ul > li{
    font-weight:500;
}
 .mobile-menu > ul li ul{
    overflow:hidden
}
 .mobile-menu ul li a{
    color:var(--menu-color);
    padding:0;
    display:block;
    transition:all .17s ease
}
.mobile-menu ul li a:hover {
color:var(--menu-hover);
}
.mobile-menu ul li a i {
    vertical-align: middle;
    margin-right: 10px;
    position: relative;
}
 .mobile-menu ul li.has-sub .submenu-toggle{
    position:absolute;
    top:0;
    right:0;
    color:var(--menu-color);
    cursor:pointer
}
 .mobile-menu ul li.has-sub .submenu-toggle:after{
    content:'\f105';
    font-family:FontAwesome;
    font-weight:900;
    float:right;
    width:34px;
    font-size:14px;
    text-align:center;
    transition:all .17s ease
}
 .mobile-menu ul li.has-sub.show > .submenu-toggle:after{
    transform:rotate(90deg)
}
 .mobile-menu > ul > li > ul > li > a{
    color:var(--menu-color);
    opacity:.7;
    padding:0 0 0 15px
}
 .mobile-menu > ul > li > ul > li > ul > li > a{
    color:var(--menu-color);
    opacity:.7;
    padding:0 0 0 30px
}
 .mm-footer{
    display:block;
    position:relative;
    float:left;
    width:100%;
    padding:20px 16px;
    margin:0
}
 .mm-footer .mm-social,.mm-footer .mm-menu{
    position:relative;
    float:left;
    width:100%;
    margin:8px 0 0
}
.mm-footer .mm-menu{
   display:none;
}
 .mm-footer .mm-social{
    margin:0
}
 .mm-footer ul{
    display:flex;
    flex-wrap:wrap
}
 .mm-footer .mm-social ul li{
    margin:0 16px 0 0
}
 .mm-footer .mm-social ul li:last-child{
    margin:0
}
 .mm-footer .mm-social ul li a{
    display:block;
    font-size:14px;
    color:var(--menu-color);
    padding:0
}
 .mm-footer .mm-social ul li a:hover{
    color:var(--menu-hover)
}
 .mm-footer .mm-menu ul li{
    margin:5px 18px 0 0
}
 .mm-footer .mm-menu ul li:last-child{
    margin:5px 0 0
}
 .mm-footer .mm-menu ul li a{
    display:block;
    font-size:14px;
    color:var(--menu-color);
    font-weight:400;
    padding:0
}
.mm-footer .mm-menu ul li a i {
    font-size: 12px;
    vertical-align: middle;
    margin-right: 6px;
    position: relative;
    top: -1px;
}
 .mm-footer .mm-menu ul li a:hover{
    color:var(--menu-hover)
}
.owl-carousel{
    display:none;
    width:100%;
    -webkit-tap-highlight-color:transparent;
    position:relative;
    z-index:1
}
 .owl-carousel .owl-stage{
    position:relative;
    -ms-touch-action:pan-Y
}
 .owl-carousel .owl-stage:after{
    content:".";
    display:block;
    clear:both;
    visibility:hidden;
    line-height:0;
    height:0
}
 .owl-carousel .owl-stage-outer{
    position:relative;
    overflow:hidden;
    -webkit-transform:translate3d(0px,0px,0px)
}
 .owl-carousel .owl-controls .owl-nav .owl-prev,.owl-carousel .owl-controls .owl-nav .owl-next,.owl-carousel .owl-controls .owl-dot{
    cursor:pointer;
    cursor:hand;
    -webkit-user-select:none;
    -khtml-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none
}
#slider-wrapper .PopularPosts .main-slider, #slider-wrapper .PopularPosts .main-slider .slider-item  {
    height: 395px;
    overflow: hidden;
}
#slider-wrapper .PopularPosts .main-slider.owl-carousel.owl-loaded, #slider-wrapper .PopularPosts .main-slider.owl-carousel.owl-loaded .slider-item  {
    height: auto;
}
 .owl-carousel.owl-loaded{
    display:block
}
 .owl-carousel.owl-loading{
    opacity:0;
    display:block
}
 .owl-carousel.owl-hidden{
    opacity:0
}
 .owl-carousel .owl-refresh .owl-item{
    display:none
}
 .owl-carousel .owl-item{
    position:relative;
    min-height:1px;
    float:left;
    -webkit-backface-visibility:visible;
    -webkit-tap-highlight-color:transparent;
    -webkit-touch-callout:none;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none
}
 .owl-carousel .owl-item img{
    display:block;
    width:100%;
    -webkit-transform-style:preserve-3d;
    transform-style:preserve-3d
}
 .owl-carousel.owl-text-select-on .owl-item{
    -webkit-user-select:auto;
    -moz-user-select:auto;
    -ms-user-select:auto;
    user-select:auto
}
 .owl-carousel .owl-grab{
    cursor:move;
    cursor:-webkit-grab;
    cursor:-o-grab;
    cursor:-ms-grab;
    cursor:grab
}
 .owl-carousel.owl-rtl{
    direction:rtl
}
 .owl-carousel.owl-rtl .owl-item{
    float:right
}
 .no-js .owl-carousel{
    display:block
}
 .owl-carousel .animated{
    -webkit-animation-duration:1000ms;
    animation-duration:1000ms;
    -webkit-animation-fill-mode:both;
    animation-fill-mode:both
}
 .owl-carousel .owl-animated-in{
    z-index:1
}
 .owl-carousel .owl-animated-out{
    z-index:0
}
 .owl-height{
    -webkit-transition:height 500ms ease-in-out;
    -moz-transition:height 500ms ease-in-out;
    -ms-transition:height 500ms ease-in-out;
    -o-transition:height 500ms ease-in-out;
    transition:height 500ms ease-in-out
}
 .owl-prev,.owl-next{
    position:relative;
    float:left;
    width:25px;
    height:30px;
    background-color:#fff;
   font-family: FontAwesome;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-size:11px;
    line-height:30px;
    font-weight:900;
    color:var(--main-dark-color);
    text-align:center;
    cursor:pointer;
    border:1px solid rgba(0,0,0,0.08);
    box-sizing:border-box;
    transition:all .25s ease
}
.is-dark .owl-prev,.is-dark .owl-next {
    background-color:#3a3a3a;
}
 .owl-prev:before{
    content:"\f053"
}
 .owl-next:before{
    content:"\f054"
}
 .owl-prev:hover,.owl-next:hover{
    background-color:var(--main-blog-color);
    color:#fff;
    border-color:var(--main-blog-color)
}
 @keyframes fadeInLeft {
     from{
        opacity:0;
        transform:translate3d(-30px,0,0)
    }
     to{
        opacity:1;
        transform:none
    }
}
 @keyframes fadeOutLeft {
     from{
        opacity:1
    }
     to{
        opacity:0;
        transform:translate3d(-30px,0,0)
    }
}
 @keyframes fadeInRight {
     from{
        opacity:0;
        transform:translate3d(30px,0,0)
    }
     to{
        opacity:1;
        transform:none
    }
}
 .fadeInRight{
    animation-name:fadeInRight
}
 @keyframes fadeOutRight {
     from{
        opacity:1
    }
     to{
        opacity:0;
        transform:translate3d(30px,0,0)
    }
}
 .fadeOutRight{
    animation-name:fadeOutRight
}
.loader{
    position:relative;
    height:280px;
    overflow:hidden;
    display:block;
    margin:0
}
 .loader:after{
    content:'';
    position:absolute;
    top:50%;
    left:50%;
    width:28px;
    height:28px;
    margin:-16px 0 0 -16px;
    border:2px solid var(--main-blog-color);
    border-right-color:rgba(155,155,155,0.2);
    border-radius:100%;
    animation:spinner 1.1s infinite linear;
    transform-origin:center
}
 @-webkit-keyframes spinner {
     0%{
        -webkit-transform:rotate(0deg);
        transform:rotate(0deg)
    }
     to{
        -webkit-transform:rotate(1turn);
        transform:rotate(1turn)
    }
}
 @keyframes spinner {
     0%{
        -webkit-transform:rotate(0deg);
        transform:rotate(0deg)
    }
     to{
        -webkit-transform:rotate(1turn);
        transform:rotate(1turn)
    }
}
#slider-wrapper .show-slider, #slider-wrapper .PopularPosts{
    display:block!important
}
#slider-wrapper .show-slider .widget-content, #slider-wrapper .PopularPosts .widget-content{
    position:relative;
    height:auto;
    overflow:hidden;
margin:30px 0 0;
}
#slider-wrapper {
    margin: 0 auto;
}
#slider-section .widget, #slider-section .widget > .widget-title {
    display: none;
}
#slider-wrapper .PopularPosts .main-slider {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    grid-gap: 10px;
}
#slider-wrapper .PopularPosts ul.main-slider.owl-carousel.owl-loaded {
    display: block;
}
 .main-slider{
    position:relative;
    overflow:hidden;
    height:auto
}
 .main-slider .slider-item{
    position:relative;
    float:left;
    width:100%;
    height:auto;
    overflow:hidden;
    box-sizing:border-box
}
#slider-wrapper .PopularPosts .main-slider .slider-item {
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
#slider-wrapper .PopularPosts ul.main-slider.owl-carousel.owl-loaded .slider-item {
    display: block;
}
 .slider-item-inner{
    position:relative;
    float:left;
    width:100%;
    height:100%;
    overflow:hidden;
    display:block;
}
 .main-slider .post-image-link{
    width:100%;
    height:280px;
    position:relative;
    overflow:hidden;
    display:block;
    margin-bottom:20px;
    background-image:linear-gradient(-45deg,rgba(0,0,0,0.1),#ededed,rgba(0,0,0,0.1));background-size:150% 150%;animation:gradient 1s ease infinite
}
@keyframes gradient {
0%{background-position:100% 50%}
50%{background-position:50% 0}
100%{background-position:100% 50%}
}
 .main-slider .post-info-wrap {
    width: 100%;
    text-align: left;
    overflow: hidden;
    z-index: 5;
    box-sizing: border-box;
    padding:0;
    transition: transform .5s ease;
}
.main-slider .owl-item.active .post-info-wrap {
   
}

 .main-slider .post-info{
  position: relative;
    overflow: hidden;
    display: block;
    z-index: 10;
}

 .main-slider .post-title{
    font-size:21px;
    font-weight:500;
    display:block;
    line-height:1.5;
    margin:0 0 5px
}
 .main-slider .post-title a{
    color:var(--title-color);
    display:block
}
 .main-slider .post-title a:hover{
    text-decoration:underline
}
.main-slider .post-snippet {
    color:$(posts.text.color);
} 
 .show-slider .no-posts{
    position:absolute;
    top:calc(50% - 50px);
    left:0;
    width:100%;
text-align:center;
}
.main-slider .post-info .post-tag{
   display: flex;
   color: var(--main-dark.color);
    font-size: 9px;
    letter-spacing: 2px;
    font-weight: 400;
    text-transform:uppercase;
    margin-bottom:15px;
}
 .main-slider .post-info .post-tag:hover{
  color:var(--main-blog-color);
}
.main-slider .post-meta {
    color: #aaaaaa;
    font-size: 12px;
    font-weight: 400;
    line-height: 18px;
    padding: 0 1px;
}
.main-slider .post-date {
    font-size: 11px;
    color: var(--main-dark-color);
    margin: 0;
display: inline-block;
float:none;
}
.main-slider .owl-nav{
    position:absolute;
    top:0;
    left:0;
    right:0;
    height:0
}
 .main-slider .owl-prev,.main-slider .owl-next{
    height:40px;
    line-height:40px;
    z-index:10;
    border:0
}
 .main-slider .owl-prev{
    float:left;
    left:-25px;
}
 .main-slider:hover .owl-prev{
    left:0
}
 .main-slider .owl-next{
    float:right;
    right:-25px;
}
 .main-slider:hover .owl-next{
    right:0
}
#main-feat-wrapper{
 margin:0
}
#featured-section {
    float: left;
    width: 100%;
    margin:0 0 30px;
    padding: 0;
}
#main-feat-wrapper .widget-content, #main-feat-wrapper .post, #main-feat-wrapper .post-content {
    display: flex;
    align-items: center;
    position: relative;
    float: left;
    width: 100%;
}
#featured-section .FeaturedPost .post-image-link {
       position: relative;
    float: left;
    flex: 1 0 310px;
    height: 250px;
    z-index: 1;
    overflow: hidden;
    margin: 0 30px 0 0;
    border-radius: 0;
}
#featured-section .FeaturedPost .post-info {
   flex-grow: 1;
    width: calc(100% - 310px);
    padding: 0;
}
#featured-section .FeaturedPost .post-info .post-title {
    font-size: 22px;
    line-height: 1.3em;
    font-weight: 600;
    margin: 0 0 15px;
}
#featured-section .FeaturedPost .post-info .post-snippet {
  line-height: 1.6em;
}
#featured-section .FeaturedPost .post-info .jump-link.flat-button a {   
   display: inline-block;
    height: 28px;
    background-color:var(--main-dark-color);
    font-size: 14px;
    color: #ffffff;
    font-weight: 500;
    line-height: 28px;
    box-sizing: border-box;
    padding: 0 12px;
    margin: 15px 0 0;
    transition: background .17s ease;
	}
.is-dark #featured-section .FeaturedPost .post-info .jump-link.flat-button a {   
color:var(--main-dark-color);
background: #666666;
}
#featured-section .FeaturedPost .post-info .jump-link.flat-button a:hover {
    background-color: var(--main-blog-color);
}
 .post-meta{
    overflow:hidden;
    color:#aaa;
    font-size:13px;
    font-weight:400;
    padding:0 1px
}
 .post-meta .post-author,.post-meta .post-date{
    display:inline-block;
    margin:0
}
.post-meta .post-author, .post-meta .post-date {

}
 .post-meta .post-author:after{
    content:'-';
    margin:0 4px
}
 .post-author{
    font-weight:700
}
 .post-meta a{
    color:var(--title-color);
    transition:color .17s
}
 .post-meta a:hover{
    color:var(--main-blog-color)
}
 .queryMessage{
    overflow:hidden;
    background-color:#f2f2f2;
    color:var(--title-color);
    font-size:13px;
    font-weight:400;
    padding:8px 10px;
    margin:0 0 25px
}
.is-dark .queryMessage{
    background-color:#3a3a3a;
}
 .queryMessage .query-info{
    margin:0 5px
}
 .queryMessage .search-query,.queryMessage .search-label{
    font-weight:700;
    text-transform:uppercase
}
 .queryMessage .search-query:before,.queryMessage .search-label:before{
    content:"\201c"
}
 .queryMessage .search-query:after,.queryMessage .search-label:after{
    content:"\201d"
}
 .queryMessage a.show-more{
    float:right;
    color:var(--title-hover);
    text-decoration:underline;
    transition:opacity .17s
}
 .queryMessage a.show-more:hover{
    opacity:.8
}
 .queryEmpty{
    font-size:13px;
    font-weight:400;
    padding:10px 0;
    margin:0 0 25px;
    text-align:center
}
 .title-wrap, #featured-section .FeaturedPost .widget-title {
    background:rgba(0,0,0,.03);
    position:relative;
    float: left;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    border-radius:3px;
    margin: 0 0 16px;
}
.is-dark .title-wrap, .is-dark #featured-section .FeaturedPost .widget-title, .is-dark .sidebar .widget-title {
    background: rgb(155 155 155 / 15%);
}
#featured-section .FeaturedPost .widget-title:after {
    content:'\efad';
    font-family:remixicon;
    font-weight: 900;
}
.title-wrap > *, #featured-section .FeaturedPost .widget-title > * {
    display: flex;
    align-items: center;
}
 .title-wrap > h3, #featured-section .FeaturedPost .widget-title > h3{
    color:var(--main-dark-color);
    margin:0;
    font-size: 16px;
    font-weight: 700;
    margin: 0;
}
.title-wrap > .title:after, #featured-section .FeaturedPost .widget-title > .title:after {
    content: '\f054';
    font-family: FontAwesome;
    font-size: 10px;
    font-weight: 900;
    line-height: 1;
    margin: 6px 0 0 3px;
}
 a.view-all{
    position:relative;
    float: right;
    font-size: 12px;
    margin:0;
    padding:0;
    font-weight: 400;
    color:var(--text-color);
    text-transform: uppercase;
    transition: all .17s ease;
}

 a.view-all:hover{
color:var(--main-blog-color);
}
 a.view-all:after{
    content:"\ed59";
    font-size: 16px;
    float:right;
    font-weight:400;
    font-family:remixicon;
    margin:0 0 0 3px;
}

#testimonial-wrap{
    display:none;
    float:left;
    width:100%;
    margin:20px 0 0
}
 #testimonial-wrap .container{
    position:relative;
    margin:0 auto
}
 #testimonial{
  display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-gap: 15px;
}
 #testimonial .widget{
display: flex;
    flex-direction: column;
    box-sizing: border-box;
    border-radius: 12px;
text-align:center;
}
 .testi-avatar{
  display:block;
    width:100%;
    height:100px;
    overflow:hidden;
    margin:0;
    border-radius: 5px;
    position:relative;
}
.testi-avatar:before {
    content: '';
    background: rgb(0 0 0 / 18%);
    height: 100%;
    width: 100%;
    position: absolute;
    left: 0;
    top: 0;
    z-index: 15;
}
 .testi-avatar img{
    display:block;
    width:100%;
    height:100%;
    object-fit:cover;
    color:transparent;
    margin:0
}
 .testi-info{
 color: #ffffff;
    background: var(--main-blog-color);
    display: inline-block;
    letter-spacing: 0.8px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    -o-transform: translate(-50%,-50%);
    -moz-transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    padding: 5px 15px;
    border-radius: 3px;
    text-transform: uppercase;
    z-index: 1515;
}
 .testi-title{
    font-size:16px;
    color:#fff;
    font-weight:500;
    margin:0
}
.testi-title a{ 
 color:#fff;
}
 .custom-widget li{
    overflow:hidden;
    margin:20px 0 0
}
 .custom-widget li:first-child{
    padding:0;
    margin:0;
    border:0
}
 .custom-widget .post-image-link{
    position:relative;
    width:80px;
    height:60px;
    float:left;
    overflow:hidden;
    display:block;
    vertical-align:middle;
    margin:0 12px 0 0;
    border-radius:4px
}
 .custom-widget .post-info{
    overflow:hidden
}
 .custom-widget .post-title{
    overflow:hidden;
    font-size:13px;
    font-weight:400;
    line-height:1.5em;
    margin:0 0 3px
}
 .custom-widget .post-title a{
    display:block;
    color:var(--title-color);
    transition:color .17s
}
 .custom-widget li:hover .post-title a{
    color:var(--title-hover)
}
 .home-ad .widget > .widget-title{
    display:none
}
 .home-ad {
    margin:0 auto
}
 .home-ad .widget .widget-content{
    position:relative;
    width:100%;
    max-height:90px;
    overflow:hidden;
    line-height:1;
    margin:30px 0 0
}
#home-ad-top2 .widget-content, #footer-ads .widget-content{
    margin: 0 0 30px;
}
#prev-ad .widget, #nxt-ad .widget {
    width: 100%;
    margin: 20px 0 0;
    border-top: 1px solid #f2f2f6;
    padding: 15px 10px 0;
    box-sizing: border-box;
}
#prev-ad .widget .widget-title , #nxt-ad .widget .widget-title {
display:none;
}
.is-dark #prev-ad .widget, .is-dark #nxt-ad .widget {
border-color:#3a3a3a;
}
#nxt-ad .widget {
    padding-bottom: 15px;
    margin-bottom: 15px;
    border-bottom: 1px solid #f2f2f6;
}
#ty-post-before-ad .widget .widget-title, #ty-post-after-ad .widget .widget-title, #ty-post-before-ad .widget .widget-title h2, #ty-post-after-ad .widget .widget-title h2 {
display:none;
}
 .index-post-wrap{
    position:relative;
    float:left;
    width:100%
}
.grid-posts {
   display: grid;
    grid-template-columns: repeat(3,1fr);
    grid-gap: 20px;
}
 .blog-post{
    display:block;
    overflow:hidden;
    word-wrap:break-word
}
 .index-post{
 position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
 .index-post .post-image-wrap{
float: left;
    width: 100%;
    height: 150px;
    overflow: hidden;
    margin: 0;
    display: flex;
}
 .index-post .post-image-wrap .post-image-link{
    width:100%;
    height:100%;
    position:relative;
    display:block;
    z-index:1;
    overflow:hidden
}
 .post-tag{
    color: #8f9294;
    text-align: left;
    margin-bottom: 10px;
    position: relative;
    font-size: 12px;
    color: #a6a7a8;
}

.blog-post .post-tag span {
text-decoration: none;
    text-transform: uppercase;
    font-style: normal;
color: var(--main-blog-color);
margin-left:5px;
}
 .index-post .post-info{
  position: relative;
    display: flex;
    flex-direction: column;
    flex: 1;
    padding: 15px 0;
}
 .index-post .post-info > h2{
   font-size: 16px;
    font-weight: 600;
    line-height:1.4em;
    text-decoration:none;
    margin:0
}
 .index-post .post-info > h2 > a{
    display:block;
    color:var(--title-color);
    transition:color .17s
}
 .index-post .post-info > h2:hover > a{
    color:var(--title-hover)
}
 .widget iframe,.widget img{
    max-width:100%
}
 .date-header{
    display:block;
    overflow:hidden;
    font-weight:400;
    margin:0!important;
    padding:0
}
 .index-post .post-meta{
    margin:10px 0 0
}
 .post-snippet{
    position:relative;
    display:block;
    overflow:hidden;
    font-size:13px;
    color:#918f94;
    line-height:1.8em;
    font-weight:400;
    margin:7px 0 0
}
 a.read-more{
    display:inline-block;
    background-color:var(--main-dark-color);
color:#fff;
    height:32px;
    font-size:12px;
    font-weight:600;
    line-height:32px;
text-transform:uppercase;
    padding:0 12px;
    margin:12px 0 0;
    transition:background .17s ease
}
 a.read-more:hover{
    background-color:var(--main-blog-color);
color:#fff;
}
 #breadcrumb{
    font-size:12px;
    font-weight:400;
    color:#aaa;
    margin:0 0 10px
}
 #breadcrumb a{
    color:#aaa;
    transition:color .17s
}
 #breadcrumb a:hover{
    color:var(--title-hover)
}
 #breadcrumb a,#breadcrumb em{
    display:inline-block
}
 #breadcrumb .delimiter:after{
    content:'\f054';
    font-family:FontAwesome;
    font-size:8px;
    font-weight:400;
    font-style:normal;
    vertical-align:middle;
    margin:0 3px
}
 .item-post h1.post-title{
    color:var(--title-color);
    font-size:27px;
    line-height:1.5em;
    font-weight:700;
    position:relative;
    display:block;
    margin:10px 0;
    padding:0
}
 .static_page .item-post h1.post-title{
    margin:0
}
 .item-post .post-body{
    width:100%;
    font-size:15px;
    line-height:1.5em;
    overflow:hidden;
    padding:20px 0 0;
    margin:10px 0 0;
    border-top:1px dashed #ebebeb
}
.is-dark .item-post .post-body {
border-color:#3a3a3a;
}
 .static_page .item-post .post-body{
    padding:20px 0
}
 .item-post .post-outer{
    padding:0
}
 .item-post .post-body img{
    max-width:100%
}
 .main .widget{
    margin:0
}
 .main .Blog{
    border-bottom-width:0
}
 .post-footer{
    position:relative;
    float:left;
    width:100%;
    margin:20px 0 0
}
 .inline-ad{
    position:relative;
    display:block;
    max-height:60px;
    margin:0 0 30px
}
 .inline-ad > ins{
    display:block!important;
    margin:0 auto!important
}
 .item .inline-ad{
    float:left;
    width:100%;
    margin:20px 0 0
}
 .item-post-wrap > .inline-ad{
    margin:0 0 20px
}
 .post-labels{
    overflow:hidden;
    height:auto;
    position:relative;
    margin:0 0 20px;
    padding:0
}
 .post-labels span,.post-labels a{
    float:left;
    height:22px;
    background-color:#f2f2f2;
    color:var(--title-color);
    font-size:12px;
    line-height:22px;
    font-weight:400;
    margin:0;
    padding:0 10px;
    border-radius:2px
}
.is-dark .post-labels span, .is-dark .post-labels a {
    background-color:#3a3a3a;
}
 .post-labels span{
    background-color:var(--main-blog-color);
    color:#fff
}
 .post-labels a{
    margin:0 0 0 5px;
    transition:all .17s ease
}
 .post-labels a:hover{
    background-color:var(--main-blog-color);
    color:#fff;
    border-color:var(--main-blog-color)
}
 .post-reactions{
    height:28px;
    display:block;
    margin:0 0 15px
}
 .post-reactions span{
    float:left;
    color:var(--title-color);
    font-size:11px;
    line-height:25px;
    text-transform:uppercase;
    font-weight:700
}
 .reactions-inner{
    float:left;
    margin:0;
    height:28px
}
 .post-share{
    position:relative;
    overflow:hidden;
    line-height:0;
    margin:0 0 30px
}
 ul.share-links{
    position:relative
}
 .share-links li{
    width:32px;
    float:left;
    box-sizing:border-box;
    margin:0 5px 0 0
}
 .share-links li.facebook,.share-links li.twitter{
    width:20%
}
 .share-links li a{
    background: rgb(0 0 0 / 30%);
    float:left;
    display:inline-block;
    cursor:pointer;
    width:100%;
    height:32px;
    line-height:32px;
    color:var(--main-dark-color);
    font-weight:400;
    font-size:13px;
    text-align:center;
    box-sizing:border-box;
    opacity:1;
    border-radius:2px;
    transition:all .17s ease
}
 .share-links li.whatsapp-mobile{
    display:none
}
 .is-mobile li.whatsapp-desktop{
    display:none
}
 .is-mobile li.whatsapp-mobile{
    display:inline-block
}
 .share-links li a:before{
    float:left;
    display:block;
    width:32px;
    background-color:rgba(0,0,0,0.05);
    text-align:center;
    line-height:32px
}
 .share-links li a:hover{
    opacity:.8
}
 ul.post-nav{
    position:relative;
    overflow:hidden;
    display:block;
    margin:0 0 30px
}
 .post-nav li{
    display:inline-block;
    width:50%
}
 .post-nav .post-prev{
    float:left;
    text-align:left;
    box-sizing:border-box;
    padding:0 10px
}
 .post-nav .post-next{
    float:right;
    text-align:right;
    box-sizing:border-box;
    padding:0 10px
}
 .post-nav li a{
    color:var(--title-color);
    line-height:1.4em;
    display:block;
    overflow:hidden;
    transition:color .17s
}
 .post-nav li:hover a{
    color:var(--title-hover)
}
 .post-nav li span{
    display:block;
    font-size:11px;
    color:#aaa;
    font-weight:700;
    text-transform:uppercase;
    padding:0 0 2px
}
 .post-nav .post-prev span:before{
    content:"\f053";
    float:left;
    font-family:FontAwesome;
    font-size:10px;
    font-weight:400;
    text-transform:none;
    margin:0 2px 0 0
}
 .post-nav .post-next span:after{
    content:"\f054";
    float:right;
    font-family:FontAwesome;
    font-size:10px;
    font-weight:400;
    text-transform:none;
    margin:0 0 0 2px
}
 .post-nav p{
    font-size:12px;
    font-weight:400;
    line-height:1.4em;
    margin:0
}
 .post-nav .post-nav-active p{
    color:#aaa
}
 .about-author{
    position:relative;
    display:block;
    overflow:hidden;
    background-color:#f9f9f9;
    padding:20px;
    margin:0 0 30px;
    border:1px solid #f0f0f0
}
.is-dark .about-author {
 background-color:#3a3a3a;
    border:1px solid #2a2a2a
}
 .about-author .avatar-container{
    position:relative;
    float:left;
    width:80px;
    height:80px;
    background-color:rgba(255,255,255,0.05);
    overflow:hidden;
    margin:0 15px 0 0
}
 .about-author .author-avatar{
    float:left;
    width:100%;
    height:100%
}
 .author-name{
    overflow:hidden;
    display:inline-block;
    font-size:12px;
    font-weight:700;
    text-transform:uppercase;
    line-height:14px;
    margin:7px 0 3px
}
 .author-name span{
    color:var(--title-color)
}
 .author-name a{
    color:var(--main-blog-color);
    transition:opacity .17s
}
 .author-name a:hover{
    opacity:.8
}
 .author-description{
    display:block;
    overflow:hidden;
    font-size:12px;
    font-weight:400;
    line-height:1.6em
}
 .author-description a:hover{
    text-decoration:underline
}
 #related-wrap{
    overflow:hidden;
    margin:0 0 30px
}
 #related-wrap .related-tag{
    display:none
}
 .related-ready{
    float:left;
    width:100%
}
 .related-ready .loader{
    height:178px
}
 ul.related-posts{
    position:relative;
    overflow:hidden;
    margin:0 -10px;
    padding:0
}
 .related-posts .related-item{
    width:33.33333333%;
    position:relative;
    overflow:hidden;
    float:left;
    display:block;
    box-sizing:border-box;
    padding:0 10px;
    margin:0
}
 .related-posts .post-image-link{
    width:100%;
    height:130px;
    position:relative;
    overflow:hidden;
    display:block;
    border-radius:4px
}
 .related-posts .post-title{
    font-size:13px;
    font-weight:400;
    line-height:1.5em;
    display:block;
    margin:7px 0 5px
}
 .related-posts .post-title a{
    color:var(--title-color);
    transition:color .17s
}
 .related-posts .related-item:hover .post-title a{
    color:var(--title-hover)
}
 #blog-pager{
    float:left;
    width:100%;
    overflow:hidden;
    clear:both;
    margin:0 0 30px
}
 .index #blog-pager, .archive #blog-pager {
    border: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}
 #blog-pager .load-more{
    display:inline-block;
    height:34px;
    background-color:var(--main-dark-color);
    font-size:14px;
    color:#ffffff;
    font-weight:400;
    line-height:34px;
    box-sizing:border-box;
    padding:0 30px;
    margin:0;
    border-radius:2px
}
 #blog-pager #load-more-link{
    color:#fff;
    cursor:pointer
}
.is-dark  #blog-pager .load-more{
    background-color:rgb(155 155 155 / 15%);
}
 #blog-pager #load-more-link:hover{
    background-color:var(--main-blog-color);
    color:#fff
}
 #blog-pager .load-more.no-more{
    background-color:rgba(155,155,155,0.05);
    color:var(--main-blog-color)
}
 #blog-pager .loading,#blog-pager .no-more{
    display:none;
    float:left;
    width:100%;
}
 #blog-pager .loading .loader{
    position:relative;
    height:100%;
    overflow:hidden;
    display:block;
    margin:0;
    display: flex;
    align-items: center;
    justify-content: center;
}
 #blog-pager .loading .loader{
    height:34px
}
 #blog-pager .no-more.show{
   display: block;
    text-align: center;
}
 #blog-pager .loading .loader:after{
    width:26px;
    height:26px;
    margin:-15px 0 0 -15px
}
 #blog-pager .loading .loader:after{
    content:'';
    position:absolute;
    top:50%;
    left:50%;
    width:28px;
    height:28px;
    margin:-16px 0 0 -16px;
    border:2px solid var(--main-blog-color);
    border-right-color:rgba(155,155,155,0.2);
    border-radius:100%;
    animation:spinner 1.1s infinite linear;
    transform-origin:center
}
 @-webkit-keyframes spinner {
     0%{
        -webkit-transform:rotate(0deg);
        transform:rotate(0deg)
    }
     to{
        -webkit-transform:rotate(1turn);
        transform:rotate(1turn)
    }
}
 @keyframes spinner {
     0%{
        -webkit-transform:rotate(0deg);
        transform:rotate(0deg)
    }
     to{
        -webkit-transform:rotate(1turn);
        transform:rotate(1turn)
    }
}

 .archive #blog-pager,.home .blog-pager .blog-pager-newer-link,.home .blog-pager .blog-pager-older-link{
    display:none
}
 .blog-post-comments{
    display:none
}
 .blog-post-comments .comments-title{
    margin:0 0 20px
}
 .comments-system-disqus .comments-title,.comments-system-facebook .comments-title{
    margin:0
}
 #comments{
    margin:0
}
 #gpluscomments{
    float:left!important;
    width:100%!important;
    margin:0 0 25px!important
}
 #gpluscomments iframe{
    float:left!important;
    width:100%
}
 .comments{
    display:block;
    clear:both;
    margin:0;
    color:var(--title-color)
}
 .comments .comment-thread > ol{
    padding:0
}
 .comments > h3{
    font-size:13px;
    font-weight:400;
    font-style:italic;
    padding-top:1px
}
 .comments .comments-content .comment{
    list-style:none;
    margin:0;
    padding:0 0 8px
}
 .comments .comments-content .comment:first-child{
    padding-top:0
}
 .facebook-tab,.fb_iframe_widget_fluid span,.fb_iframe_widget iframe{
    width:100%!important
}
 .comments .item-control{
    position:static
}
 .comments .avatar-image-container{
    float:left;
    overflow:hidden;
    position:absolute
}
 .comments .avatar-image-container,.comments .avatar-image-container img{
    height:35px;
    max-height:35px;
    width:35px;
    max-width:35px;
    border-radius:100%
}
 .comments .comment-block{
    overflow:hidden;
    padding:0 0 10px
}
 .comments .comment-block,.comments .comments-content .comment-replies{
    margin:0 0 0 50px
}
 .comments .comments-content .inline-thread{
    padding:0
}
 .comments .comment-actions{
    float:left;
    width:100%;
    position:relative;
    margin:0
}
 .comments .comments-content .comment-header{
    font-size:15px;
    display:block;
    overflow:hidden;
    clear:both;
    margin:0 0 3px;
    padding:0 0 5px;
    border-bottom:1px dashed #d6d6d6
}
 .comments .comments-content .comment-header a{
    color:var(--title-color);
    transition:color .17s
}
 .comments .comments-content .comment-header a:hover{
    color:var(--title-hover)
}
 .comments .comments-content .user{
    font-style:normal;
    font-weight:700;
    display:block
}
 .comments .comments-content .icon.blog-author{
    display:none
}
 .comments .comments-content .comment-content{
    float:left;
    font-size:13px;
    color:#5E5E5E;
    font-weight:400;
    text-align:left;
    line-height:1.4em;
    margin:5px 0 9px
}
 .comments .comment .comment-actions a{
    margin-right:5px;
    padding:2px 5px;
    color:var(--title-color);
    font-weight:400;
    background-color:#f2f2f2;
    font-size:10px;
    transition:all .17s ease;
}
.is-dark .comments .comment .comment-actions a{ 
    background-color:#3a3a3a;
}
 .comments .comment .comment-actions a:hover{
    color:#fff;
    background-color:var(--main-blog-color);
    border-color:var(--main-blog-color);
    text-decoration:none
}
 .comments .comments-content .datetime{
    float:left;
    font-size:11px;
    font-weight:400;
    color:#aaa;
    position:relative;
    padding:0 1px;
    margin:4px 0 0;
    display:block
}
 .comments .comments-content .datetime a,.comments .comments-content .datetime a:hover{
    color:#aaa
}
 .comments .thread-toggle{
    margin-bottom:4px
}
 .comments .thread-toggle .thread-arrow{
    height:7px;
    margin:0 3px 2px 0
}
 .comments .thread-count a,.comments .continue a{
    transition:opacity .17s
}
 .comments .thread-count a:hover,.comments .continue a:hover{
    opacity:.8
}
 .comments .thread-expanded{
    padding:5px 0 0
}
 .comments .thread-chrome.thread-collapsed{
    display:none
}
 .thread-arrow:before{
    content:'';
    font-family:FontAwesome;
    color:var(--title-color);
    font-weight:400;
    margin:0 2px 0 0
}
 .comments .thread-expanded .thread-arrow:before{
    content:'\f0d7'
}
 .comments .thread-collapsed .thread-arrow:before{
    content:'\f0da'
}
 .comments .comments-content .comment-thread{
    margin:0
}
 .comments .continue a{
    padding:0 0 0 60px;
    font-weight:400
}
 .comments .comments-content .loadmore.loaded{
    margin:0;
    padding:0
}
 .comments .comment-replybox-thread{
    margin:0
}
 .comments .comments-content .loadmore,.comments .comments-content .loadmore.loaded{
    display:none
}
 #comment-editor{
    margin:0 0 20px
}
 .post-body h1,.post-body h2,.post-body h3,.post-body h4,.post-body h5,.post-body h6{
    color:var(--title-color);
    font-weight:700;
    margin:0 0 15px
}
 .post-body h1,.post-body h2{
    font-size:24px
}
 .post-body h3{
    font-size:21px
}
 .post-body h4{
    font-size:18px
}
 .post-body h5{
    font-size:16px
}
 .post-body h6{
    font-size:13px
}
 blockquote{
    font-style:italic;
    padding:10px;
    margin:0;
    border-left:4px solid var(--main-blog-color)
}
 blockquote:before,blockquote:after{
    display:inline-block;
    font-family:FontAwesome;
    font-style:normal;
    font-weight:400;
    color:#aaa;
    line-height:1
}
 blockquote:before{
    content:'\f10d';
    margin:0 10px 0 0
}
 blockquote:after{
    content:'\f10e';
    margin:0 0 0 10px
}
 .widget .post-body ul,.widget .post-body ol{
    line-height:1.5;
    font-weight:400
}
 .widget .post-body li{
    margin:5px 0;
    padding:0;
    line-height:1.5
}
 .post-body ul{
    padding:0 0 0 20px
}
 .post-body ul li:before{
    content:"\f105";
    font-family:FontAwesome;
    font-size:13px;
    font-weight:400;
    margin:0 5px 0 0
}
 .post-body u{
    text-decoration:underline
}
 .post-body a{
    transition:color .17s ease
}
 .post-body strike{
    text-decoration:line-through
}
 .contact-form{
    overflow:hidden
}
 .contact-form .widget-title{
    display:none
}
 .contact-form .contact-form-name{
    width:calc(50% - 5px)
}
 .contact-form .contact-form-email{
    width:calc(50% - 5px);
    float:right
}
.sidebar {

}
 .sidebar .widget{
    position:relative;
    overflow:hidden;
    box-sizing:border-box;
    padding:0;
    margin:0 0 30px
}
 .sidebar .widget-title{
  background:rgba(0,0,0,.03);
    position:relative;
    float: left;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    border-radius:3px;
    margin: 0 0 16px;
}
 .sidebar .widget-title > h3{
    color: var(--title-color);
    margin: 0;
    font-size: 16px;
    font-weight: 700;
    margin: 0;
}
 .sidebar .widget-content{
    float:left;
    width:100%;
    margin:0
}
 ul.social-counter{
    margin:0 -5px
}
 .social-counter li{
    float:left;
    width:25%;
    box-sizing:border-box;
    padding:0 5px;
    margin:10px 0 0
}
 .social-counter li:nth-child(1),.social-counter li:nth-child(2),.social-counter li:nth-child(3),.social-counter li:nth-child(4){
    margin-top:0
}
 .social-counter li a{
    display:block;
    height:40px;
    font-size:22px;
    color:var(--main-dark-color);
    border:1px solid rgba(155,155,155,0.15);
    text-align:center;
    line-height:40px;
    border-radius:2px;
    transition:opacity .17s
}
 .social-counter li a:hover{
    border-color:var(--main-blog-color);
}
 .list-label li{
    position:relative;
    display:block;
    padding:7px 0;
    border-top:1px dotted #ebebeb
}
.is-dark .list-label li{
    border-color:#3a3a3a
}
 .list-label li:first-child{
    padding-top:0;
    border-top:0
}
 .list-label li:last-child{
    padding-bottom:0;
    border-bottom:0
}
 .list-label li a{
    display:block;
    color:var(--title-color);
    font-size:12px;
    font-weight:400;
    text-transform:capitalize;
    transition:color .17s
}
 .list-label li a:before{
    content:"\f054";
    float:left;
    color:var(--title-color);
    font-weight:400;
    font-family:FontAwesome;
    font-size:6px;
    margin:5px 3px 0 0;
    transition:color .17s
}
 .list-label li a:hover{
    color:var(--title-hover)
}
 .list-label .label-count{
    position:relative;
    float:right;
    width:16px;
    height:16px;
    background-color:var(--main-blog-color);
    color:#fff;
    font-size:11px;
    font-weight:400;
    text-align:center;
    line-height:16px;
    border-radius:2px
}
 .cloud-label li{
    position:relative;
    float:left;
    margin:0 5px 5px 0
}
 .cloud-label li a{
    display:block;
    height:26px;
    background-color:#f2f2f2;
    color:var(--title-color);
    font-size:12px;
    line-height:26px;
    font-weight:400;
    padding:0 10px;
    border-radius:2px;
    transition:all .17s ease
}
.is-dark .cloud-label li a {
    background-color:#3a3a3a;
}
 .cloud-label li a:hover{
    color:#fff;
    background-color:var(--main-blog-color)
}
 .cloud-label .label-count{
    display:none
}
 .sidebar .FollowByEmail > .widget-title > h3{
    margin:0
}
 .FollowByEmail .widget-content{
    position:relative;
    overflow:hidden;
    background-color:#f9f9f9;
    text-align:center;
    font-weight:400;
    box-sizing:border-box;
    padding:20px;
    border-radius:2px;
    border:1px solid #f0f0f0
}
 .FollowByEmail .widget-content > h3{
    font-size:18px;
    color:var(--title-color);
    font-weight:700;
    text-transform:uppercase;
    margin:0 0 13px
}
 .FollowByEmail .before-text{
    font-size:13px;
    line-height:1.5em;
    margin:0 0 15px;
    display:block;
    padding:0 10px;
    overflow:hidden
}
 .FollowByEmail .widget-content:after{
    content:'\f0e0';
    position:absolute;
    right:-15px;
    top:-15px;
    font-family:FontAwesome;
    font-size:50px;
    color:#f0f0f0;
    transform:rotate(21deg)
}
 .FollowByEmail .follow-by-email-inner{
    position:relative
}
 .FollowByEmail .follow-by-email-inner .follow-by-email-address{
    width:100%;
    height:32px;
    color:var(--title-color);
    font-size:11px;
    font-family:inherit;
    padding:0 10px;
    margin:0 0 10px;
    box-sizing:border-box;
    border:1px solid #f0f0f0;
    border-radius:2px;
    transition:ease .17s
}
 .FollowByEmail .follow-by-email-inner .follow-by-email-submit{
    width:100%;
    height:32px;
    font-family:inherit;
    font-size:11px;
    color:#fff;
    background-color:var(--main-blog-color);
    text-transform:uppercase;
    text-align:center;
    font-weight:700;
    cursor:pointer;
    margin:0;
    border:0;
    border-radius:2px;
    transition:opacity .17s ease
}
 .FollowByEmail .follow-by-email-inner .follow-by-email-submit:hover{
    opacity:.85
}
 #ArchiveList ul.flat li{
    color:var(--title-color);
    font-size:13px;
    font-weight:400;
    padding:7px 0;
    border-bottom:1px dotted #eaeaea
}
 #ArchiveList ul.flat li:first-child{
    padding-top:0
}
 #ArchiveList ul.flat li:last-child{
    padding-bottom:0;
    border-bottom:0
}
 #ArchiveList .flat li > a{
    display:block;
    color:var(--title-color);
    transition:color .17s
}
 #ArchiveList .flat li > a:hover{
    color:var(--title-hover)
}
 #ArchiveList .flat li > a:before{
    content:"\f054";
    float:left;
    color:#161619;
    font-weight:400;
    font-family:FontAwesome;
    font-size:6px;
    margin:5px 4px 0 0;
    display:inline-block;
    transition:color .17s
}
 #ArchiveList .flat li > a > span{
    position:relative;
    float:right;
    width:16px;
    height:16px;
    background-color:var(--main-blog-color);
    color:#fff;
    font-size:11px;
    font-weight:400;
    text-align:center;
    line-height:16px;
    border-radius:2px
}
 .PopularPosts .default-popularpost{
    overflow:hidden;
    margin:20px 0 0
}
 .PopularPosts .default-popularpost .post:first-child{
    padding:0;
    margin:0;
    border:0
}
 .PopularPosts .default-popularpost .post-image-link{
    position:relative;
    width:80px;
    height:60px;
    float:left;
    overflow:hidden;
    display:block;
    vertical-align:middle;
    margin:0 12px 0 0;
    border-radius:4px
}
 .PopularPosts .default-popularpost .post-info{
    overflow:hidden
}
 .PopularPosts .default-popularpost .post-title{
    font-size:13px;
    font-weight:400;
    line-height:1.5em;
    margin:0 0 3px
}
 .PopularPosts .default-popularpost .post-title a{
    display:block;
    color:var(--title-color);
    transition:color .17s
}
 .PopularPosts .default-popularpost:hover .post-title a{
    color:var(--title-hover)
}
 .PopularPosts .default-popularpost .post-date:before{
    font-size:10px
}
 .FeaturedPost .post-image-link{
    display:block;
    position:relative;
    width:100%;
    height:180px;
    overflow:hidden;
    margin:0 0 10px;
    border-radius:4px
}
 .FeaturedPost .post-title{
    font-size:16px;
    overflow:hidden;
    font-weight:400;
    line-height:1.5em;
    margin:0 0 5px
}
 .FeaturedPost .post-title a{
    color:var(--title-color);
    display:block;
    transition:color .17s ease
}
 .FeaturedPost .post-title a:hover{
    color:var(--title-hover)
}
 .Text{
    font-size:13px
}
 .contact-form-widget form{
    font-weight:400
}
 .contact-form-name{
    float:left;
    width:100%;
    height:30px;
    font-family:inherit;
    font-size:13px;
    line-height:30px;
    box-sizing:border-box;
    padding:5px 10px;
    margin:0 0 10px;
    border:1px solid #ebebeb;
    border-radius:2px
}
 .contact-form-email{
    float:left;
    width:100%;
    height:30px;
    font-family:inherit;
    font-size:13px;
    line-height:30px;
    box-sizing:border-box;
    padding:5px 10px;
    margin:0 0 10px;
    border:1px solid #ebebeb;
    border-radius:2px
}
 .contact-form-email-message{
    float:left;
    width:100%;
    font-family:inherit;
    font-size:13px;
    box-sizing:border-box;
    padding:5px 10px;
    margin:0 0 10px;
    border:1px solid #ebebeb;
    border-radius:2px
}
.is-dark .contact-form-name, .is-dark .contact-form-email, .is-dark .contact-form-email-message {
background:#3a3a3a;
border-color:#2a2a2a;
color:#ffffff;
}
 .contact-form-button-submit{
    float:left;
    width:100%;
    height:30px;
    background-color:var(--main-blog-color);
    font-size:13px;
    color:#fff;
    line-height:30px;
    cursor:pointer;
    box-sizing:border-box;
    padding:0 10px;
    margin:0;
    border:0;
    border-radius:2px;
    transition:background .17s ease
}
 .contact-form-button-submit:hover{
    background-color:var(--main-dark-color)
}
 .contact-form-error-message-with-border{
    float:left;
    width:100%;
    background-color:#fbe5e5;
    font-size:11px;
    text-align:center;
    line-height:11px;
    padding:3px 0;
    margin:10px 0;
    box-sizing:border-box;
    border:1px solid #fc6262
}
 .contact-form-success-message-with-border{
    float:left;
    width:100%;
    background-color:#eaf6ff;
    font-size:11px;
    text-align:center;
    line-height:11px;
    padding:3px 0;
    margin:10px 0;
    box-sizing:border-box;
    border:1px solid #5ab6f9
}
 .contact-form-cross{
    margin:0 0 0 3px
}
 .contact-form-error-message,.contact-form-success-message{
    margin:0
}
 .BlogSearch .search-input{
    float:left;
    width:75%;
    height:30px;
    background-color:#fff;
    font-weight:400;
    font-size:13px;
    line-height:30px;
    box-sizing:border-box;
    padding:5px 10px;
    border:1px solid #ebebeb;
    border-right-width:0;
    border-radius:2px 0 0 2px
}
 .BlogSearch .search-action{
    float:right;
    width:25%;
    height:30px;
    font-family:inherit;
    font-size:13px;
    line-height:30px;
    cursor:pointer;
    box-sizing:border-box;
    background-color:var(--main-blog-color);
    color:#fff;
    padding:0 5px;
    border:0;
    border-radius:0 2px 2px 0;
    transition:background .17s ease
}
 .BlogSearch .search-action:hover{
    background-color:var(--main-dark-color)
}
 .Profile .profile-img{
    float:left;
    width:80px;
    height:80px;
    margin:0 15px 0 0;
    transition:all .17s ease
}
 .Profile .profile-datablock{
    margin:0
}
 .Profile .profile-data .g-profile{
    display:block;
    font-size:18px;
    color:var(--title-color);
    font-weight:700;
    margin:0 0 5px;
    transition:color .17s ease
}
 .Profile .profile-data .g-profile:hover{
    color:var(--title-hover)
}
 .Profile .profile-info > .profile-link{
    color:var(--title-color);
    font-size:11px;
    margin:5px 0 0;
    transition:color .17s ease
}
 .Profile .profile-info > .profile-link:hover{
    color:var(--title-hover)
}
 .Profile .profile-datablock .profile-textblock{
    display:none
}
 .common-widget .LinkList ul li,.common-widget .PageList ul li{
    width:calc(50% - 5px);
    padding:7px 0 0
}
 .common-widget .LinkList ul li:nth-child(odd),.common-widget .PageList ul li:nth-child(odd){
    float:left
}
 .common-widget .LinkList ul li:nth-child(even),.common-widget .PageList ul li:nth-child(even){
    float:right
}
 .common-widget .LinkList ul li a,.common-widget .PageList ul li a{
    display:block;
    color:var(--title-color);
    font-size:13px;
    font-weight:400;
    transition:color .17s ease
}
 .common-widget .LinkList ul li a:hover,.common-widget .PageList ul li a:hover{
    color:var(--title-hover)
}
 .common-widget .LinkList ul li:first-child,.common-widget .LinkList ul li:nth-child(2),.common-widget .PageList ul li:first-child,.common-widget .PageList ul li:nth-child(2){
    padding:0
}
 #footer-wrapper{
    background-color:var(--footer-bg);
    border-top:1px solid rgba(158, 158, 158, 0.23);
    position: relative;
}
 #sub-footer-wrapper{
    color:var(--footer-color);
    display:block;
    padding:0;
    width:100%;
    overflow:hidden;
}
 #sub-footer-wrapper .container{
    overflow:hidden;
    margin:0 auto;
    padding:10px 0
}
 #menu-footer{
    float:right;
    position:relative;
    display:block
}
 #menu-footer .widget > .widget-title{
    display:none
}
 #menu-footer ul li{
    float:left;
    display:inline-block;
    height:34px;
    padding:0;
    margin:0
}
 #menu-footer ul li a{
    font-size:12px;
    font-weight:400;
    display:block;
    color:var(--footer-color);
    line-height:34px;
    padding:0 10px;
    margin:0 0 0 5px;
    transition:color .17s ease
}
#menu-footer ul li a i {
    font-size: 16px;
    vertical-align: middle;
    margin-right: 6px;
    position: relative;
    top: -1px;
}
 #menu-footer ul li:last-child a{
    padding:0 0 0 5px
}
 #menu-footer ul li a:hover{
    color:$(footer.hover)
}
 #sub-footer-wrapper .copyright-area{
    font-size:12px;
    float:left;
    height:34px;
    line-height:34px;
    font-weight:400
}
 #sub-footer-wrapper .copyright-area a{
    color:$(footer.hover);
    transition:color .17s
}
#sub-footer-wrapper .copyright-area a:hover{
    color:var(--footer-color);
}
.mobile-foot-menu {
    display:none;
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: var(--footer-bg);
    border-top: 1px solid rgba(158, 158, 158, 0.23);
    border-radius: 0px 0px 0 0;
    box-shadow: 0 5px 15px 0 rgb(0 0 0 / 12%);
    z-index: 1;
}
.mobile-foot-menu .mobile-foot-menu-wrapper {
    margin:0;
    height:50px;
    display: grid;
    grid-template-columns: repeat(5,1fr);
    grid-gap: 0;
}
.mobile-foot-menu .mobile-foot-menu-wrapper span {
    display: flex;
    flex-direction: column;
    text-align: center;
    justify-content: center;
    cursor: pointer;
    border-right: 1px solid rgba(158, 158, 158, 0.23);
    transition: all .17s ease;
}
.mobile-foot-menu .mobile-foot-menu-wrapper span:last-child {
border:0;
}
.mobile-foot-menu .mobile-foot-menu-wrapper span:before {
    content:'';
    font-size: 22px;
    font-weight: 400;
    font-family: remixicon;
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-home:before {
    display:none;
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-home a:before {
     content: "\edd6";     
    font-size: 22px;
    font-weight: 400;
    font-family: remixicon;   
    color:var(--text-color);
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-search:before {
       content: "\f037";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-menu:before {
       content: "\ed59";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-dark:before {
    content: "\eefb";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-top:before {
       content: "\ec54";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-home a:hover:before {
      content: "\edd1";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-search:hover:before {
       content: "\f036";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-menu:hover:before {
       content: "\ed58";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-dark:hover:before {
    content: "\eef8";
}
.mobile-foot-menu .mobile-foot-menu-wrapper .mobile-foot-menu-top:hover:before {
       content: "\ec53";
}
 .hidden-widgets{
    display:none;
    visibility:hidden
}
 .back-top{
    display:none;
    z-index:1010;
    width:32px;
    height:32px;
    position:fixed;
    bottom:25px;
    right:25px;
    cursor:pointer;
    overflow:hidden;
    font-size:13px;
    color:#fff;
    text-align:center;
    line-height:32px;
    border-radius:2px
}
 .back-top:before{
    content:'';
    position:absolute;
    top:0;
    left:0;
    right:0;
    bottom:0;
    background-color:var(--main-blog-color);
    opacity:.5;
    transition:opacity .17s ease
}
 .back-top:after{
    content:'\f077';
    position:relative;
    font-family:FontAwesome;
    font-weight:400;
    opacity:.8;
    transition:opacity .17s ease
}
 .back-top:hover:before,.back-top:hover:after,.nav-active .back-top:after,.nav-active .back-top:before{
    opacity:1
}
 .error404 #main-wrapper{
    width:100%!important;
    margin:0!important
}
 .error404 #sidebar-wrapper{
    display:none
}
 .errorWrap{
    color:var(--title-color);
    text-align:center;
    padding:80px 0 100px
}
 .errorWrap h3{
    font-size:160px;
    line-height:1;
    margin:0 0 30px
}
 .errorWrap h4{
    font-size:25px;
    margin:0 0 20px
}
 .errorWrap p{
    margin:0 0 10px
}
 .errorWrap a{
    display:block;
    color:var(--main-blog-color);
    padding:10px 0 0
}
 .errorWrap a i{
    font-size:20px
}
 .errorWrap a:hover{
    text-decoration:underline
}
 @media screen and (max-width: 1500px) {
     .mobile-side-menu {
      width: 250px;
      }
     .header-header .flex-left {
    max-width: 350px;
}
     #outer-wrapper{
        max-width:100%;
        margin-left: 250px;
    }
     .row{
        width:100%
    }
     .top-bar .container{
        box-sizing:border-box;
        padding:0 20px
    }
     #header-wrap{
        height:auto
    }
     .header-header{
        height:auto;
        box-sizing:border-box;
        padding:25px 20px
    }
  #slider-section {
    padding: 0 20px;
    box-sizing: border-box;
}
.home-ad {
    padding: 0 20px;
    box-sizing: border-box;
}
#featured-section .FeaturedPost .post-image-link {
    flex: 1 0 180px;
    height: 110px;
}
#featured-section .FeaturedPost .post-info {
    width: calc(100% - 180px);
}
#featured-section .FeaturedPost .post-info .post-snippet {
    display: none;
}
#featured-section .FeaturedPost .post-info .jump-link.flat-button {
    display: none;
}
#featured-section .FeaturedPost .post-info .post-title {
    font-size: 18px;
}
.grid-posts {
    grid-template-columns: repeat(2,1fr);
}
     #content-wrapper{
        position:relative;
        box-sizing:border-box;
        padding:0 20px;
        margin:30px 0 0
    }
     #footer-wrapper .container{
        box-sizing:border-box;
        padding:25px 20px
    }
     #sub-footer-wrapper .container{
        box-sizing:border-box;
        padding:10px 20px
    }
}
@media screen and (min-width: 981px) {
.mobile-foot-menu {
    display: none!important;
}
}
 @media screen and (max-width: 980px) {
     .mobile-menu-toggle {
    display: flex;
    left: 0;
    position: absolute;
    text-align: left;
    justify-content: flex-start;
}
.search-menu-toggle {
    display: flex;
    right: 0;
    text-align: right;
    position: absolute;
    justify-content: flex-end;
}
     .mobile-logo {
      display: flex;
      }
     .mobile-search, .tgl-wrap {
      display: none;
      }
      .search-active .full-screen-search  .mobile-search {
      display: block;
    padding: 0 20px;
    box-sizing: border-box;
      }
     .mobile-side-menu {   
    width: 300px;
      visibility:hidden;
    opacity: 0;
      -webkit-transform: translateX(-100%);
    transform: translateX(-100%);
      }
      .nav-active .mobile-side-menu {
    visibility: visible;
    opacity: 1;
    z-index: 151515;
    transform: scaleY(1);
      }
.hide-freepic-pro-mobile-menu {
    display: flex;
}
      #outer-wrapper {
      margin: 0 auto;
      }
      .back-top {
      display:none!important;
      }
      #footer-wrapper {
       padding-bottom: 50px;
      }
     #content-wrapper > .container{
        margin:0
    }
     #header-wrap{
        padding:0
    }
     .header-header{
        padding:0
    }
     .header-header .container {
      padding: 0 20px;
    box-sizing: border-box;
    }
     #header-inner a{
        display:inline-block!important
    }
     #main-wrapper,#sidebar-wrapper{
        width:100%;
        padding:0
    }
     .item #sidebar-wrapper{
        margin-top:20px
    }
}
 @media screen and (max-width: 880px) {
.header-header .flex-left {
   max-width: 100%;
    justify-content: center;
}
.header-header .flex-left .top-bar-nav, .header-header .flex-right {
    display: none;
}
.mm-footer .mm-menu {
display:block;
}
.header-logo {
    text-align: left;
}
     .footer-widgets-wrap{
        display:block
    }
     #footer-wrapper .footer{
        width:100%;
        margin-right:0
    }
     #footer-sec2,#footer-sec3{
        margin-top:25px
    }
}
@media screen and (max-width: 769px) {
#slider-wrapper .PopularPosts .main-slider {
    grid-template-columns: repeat(2,1fr);
}
}
@media screen and (max-width: 681px) {
#slider-wrapper .PopularPosts .main-slider {
        grid-template-columns: 1fr;
    grid-gap: 0px;
}
}
 @media screen and (max-width: 680px) {
.post-read-link {
    display: none;
}
     .index-post{
        width:100%
    }
     #menu-footer,#sub-footer-wrapper .copyright-area{
        width:100%;
        height:auto;
        line-height:inherit;
        text-align:center
    }
     #menu-footer{
        margin:10px 0 0
    }
     #sub-footer-wrapper .copyright-area{
        margin:10px 0
    }
     #menu-footer ul li{
        float:none;
        height:auto
    }
     #menu-footer ul li a{
        line-height:inherit;
        margin:0 3px 5px
    }
}
 @media screen and (max-width: 560px) {
.mobile-logo {
    max-width: 180px;
}
.main-slider .post-title {
    font-size: 18px;
}
     .top-bar{
        display:none
    }
#main-feat-wrapper .post-content {
    display: block;
}
#featured-section .FeaturedPost .post-image-link {
    width: 100%;
    margin: 0 0 15px;
    height: 150px;
}
#featured-section .FeaturedPost .post-info {
    width: 100%;
    float: left;
    display: block;
}
#featured-section .FeaturedPost .post-info .post-snippet {
    display: block;
}
#featured-section .FeaturedPost .post-info .jump-link.flat-button {
    display: inline-block;
}
.grid-posts {
    grid-template-columns: 1fr;
}
.index-post .post-info > h2 {
    font-size: 20px;
    line-height: 1.3em;
}
.post-snippet {
    font-size: 13px;
    line-height: 1.8em;
}
     .share-links li a span{
        display:none
    }
     .share-links li.facebook,.share-links li.twitter{
        width:32px
    }
     ul.related-posts{
        margin:0
    }
     .related-posts .related-item{
        width:100%;
        padding:0;
        margin:20px 0 0
    }
     .related-posts .item-0{
        margin:0
    }
     .related-posts .post-tag{
        display:none
    }
     .related-posts .post-image-link{
        width:80px;
        height:60px;
        float:left;
        margin:0 12px 0 0
    }
     .related-posts .post-title{
        font-size:13px;
        overflow:hidden;
        margin:0 0 5px
    }
     .post-reactions{
        display:none
    }
}
 @media screen and (max-width: 440px) {
     .queryMessage{
        text-align:center
    }
     .queryMessage a.show-more{
        width:100%;
        margin:10px 0 0
    }
     .item-post h1.post-title{
        font-size:24px
    }
     .about-author{
        text-align:center
    }
     .about-author .avatar-container{
        float:none;
        display:table;
        margin:0 auto 10px
    }
     #comments ol{
        padding:0
    }
     .errorWrap{
        padding:70px 0 100px
    }
     .errorWrap h3{
        font-size:120px
    }
}
 @media screen and (max-width: 360px) {
 .mobile-side-menu{
        width:100%
    }
    .title-wrap > h3:before {
display:none;
}
.title-wrap > h3 {
    font-size: 15px;
}
     .about-author .avatar-container{
        width:60px;
        height:60px
    }
}

]]></b:skin>
<style>
  .firstcharacter{
    float:left;
    color:#27ae60;
    font-size:75px;
    line-height:60px;
    padding-right:8px;
}
 .post-body p{
    margin-bottom:25px
}
 .post-body h1,.post-body h2,.post-body h3,.post-body h4,.post-body h5,.post-body h6{
    line-height:1.3em;
    margin:0 0 20px
}
 .post-body img{
    height:auto!important
}
 blockquote{
    position:relative;
    background-color:rgba(155,155,155,0.05);
    font-style:normal;
    padding:20px 25px;
    margin:0;
    border-radius:3px
}
 blockquote:before{
    position:absolute;
    left:10px;
    top:10px;
    content:&#39;\f10e&#39;;
    font-family:FontAwesome;
    font-size:33px;
    font-style:normal;
    font-weight:900;
    color:#000;
    line-height:1;
    opacity:.05;
    margin:0
}
 .post-body .responsive-video-wrap{
    position:relative;
    width:100%;
    padding:0;
    padding-top:56%
}
 .post-body .responsive-video-wrap iframe{
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%
}
 .post-body ul{
    padding:0 0 0 15px;
    margin:10px 0
}
 .post-body li{
    margin:5px 0;
    padding:0
}
 .post-body ul li,.post-body ol ul li{
    list-style:none
}
 .post-body ul li:before{
    display:inline-block;
    content:&#39;\2022&#39;;
    margin:0 5px 0 0
}
 .post-body ol{
    counter-reset:ify;
    padding:0 0 0 45px;
    margin:10px 0
}
 .post-body ol &gt; li{
    counter-increment:ify;
    list-style:none
}
 .post-body ol &gt; li:before{
    display:inline-block;
    content:counters(ify,&#39;.&#39;)&#39;.&#39;;
    margin:0 5px 0 0
}
 .post-body u{
    text-decoration:underline
}
 .post-body strike{
    text-decoration:line-through
}
 .post-body sup{
    vertical-align:super
}
 .post-body a{
  
}
 .post-body a:hover{
}
 .post-body a.button{
    display:inline-block;
    height:34px;
    background-color:#2c3e50;
    font-size:14px;
    color:#ffffff;
    font-weight:400;
    line-height:34px;
    text-align:center;
    text-decoration:none;
    cursor:pointer;
    padding:0 20px;
    margin:0 6px 8px 0
}
 .post-body a.colored-button{
    color:#fff
}
 .post-body a.button:hover{
    background-color:#f47500;
    color:#fff
}
 .post-body a.colored-button:hover{
    background-color:#f47500!important;
    color:#fff!important
}
 .button:before{
    float:left;
    font-family:FontAwesome;
    font-weight:900;
    display:inline-block;
    margin:0 8px 0 0
}
 .button.preview:before{
    content:&#39;\f06e&#39;
}
 .button.download:before{
    content:&#39;\f019&#39;
}
 .button.link:before{
    content:&#39;\f0c1&#39;
}
 .button.cart:before{
    content:&#39;\f07a&#39;
}
 .button.info:before{
    content:&#39;\f06a&#39;
}
 .button.share:before{
    content:&#39;\f1e0&#39;
}
 .button.contact:before{
    content:&#39;\f0e0&#39;;
    font-weight:400
}
 .alert-message{
    position:relative;
    display:block;
    padding:15px;
    border:1px solid rgba(155,155,155,0.1);
    border-radius:3px
}
 .alert-message.alert-success{
    background-color:rgba(34,245,121,0.03);
    border:1px solid rgba(34,245,121,0.5)
}
 .alert-message.alert-info{
    background-color:rgba(55,153,220,0.03);
    border:1px solid rgba(55,153,220,0.5)
}
 .alert-message.alert-warning{
    background-color:rgba(185,139,61,0.03);
    border:1px solid rgba(185,139,61,0.5)
}
 .alert-message.alert-error{
    background-color:rgba(231,76,60,0.03);
    border:1px solid rgba(231,76,60,0.5)
}
 .alert-message:before{
    font-family:FontAwesome;
    font-size:16px;
    font-weight:900;
    display:inline-block;
    margin:0 5px 0 0
}
 .alert-message.alert-success:before{
    content:&#39;\f058&#39;;
    color:rgba(34,245,121,1)
}
 .alert-message.alert-info:before{
    content:&#39;\f05a&#39;;
    color:rgba(55,153,220,1)
}
 .alert-message.alert-warning:before{
    content:&#39;\f06a&#39;;
    color:rgba(185,139,61,1)
}
 .alert-message.alert-error:before{
    content:&#39;\f057&#39;;
    color:rgba(231,76,60,1)
}
 .post-body table{
    width:100%;
    overflow-x:auto;
    text-align:left;
    margin:0;
    border-collapse:collapse;
    border:1px solid #161619
}
 
 .post-body table td,.post-body table th{
    padding:7px 15px;
    border:1px solid #161619
}

 .post-body table thead th{
    font-weight:700;
    text-align:left;
    vertical-align:bottom
}
 table.tr-caption-container,table.tr-caption-container td,table.tr-caption-container th{
    line-height:1;
    padding:0;
    border:0
}
 table.tr-caption-container td.tr-caption{
    font-size:13px;
    color:#666666;
    padding:6px 0 0
}
 .tocify-wrap{
    display:flex;
    width:100%;
    clear:both;
    margin:0
}
 .tocify-inner{
    position:relative;
    max-width:100%;
    background-color:rgba(155,155,155,0.05);
    display:flex;
    flex-direction:column;
    overflow:hidden;
    font-size:14px;
    color:#000000;
    line-height:1.6em;
    border:1px solid rgba(155,155,155,0.1);
    border-radius:3px
}
 a.tocify-title{
    position:relative;
    height:38px;
    font-size:16px;
    color:#000000;
    font-weight:700;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 15px;
    margin:0
}
  .is-dark a.tocify-title {
  color:#f2f2f2;
  }
 .tocify-title-text{
    display:flex
}
 .tocify-title-text:before{
    content:&#39;\f0cb&#39;;
    font-family:FontAwesome;
    font-size:14px;
    font-weight:900;
    margin:0 6px 0 0
}
 .tocify-title:after{
    content:&#39;\f078&#39;;
    font-family:FontAwesome;
    font-size:12px;
    font-weight:900;
    margin:0 0 0 25px
}
 .tocify-title.is-expanded:after{
    content:&#39;\f077&#39;
}
 a.tocify-title:hover{
    text-decoration:none
}
 #tocify{
    display:none;
    padding:0 15px 10px;
    margin:0
}
 #tocify ol{
    padding:0 0 0 15px
}
 .rtl #tocify ol{
    padding:0 15px 0 0
}
 #tocify li{
    font-size:14px;
    margin:8px 0
}
 #tocify li a{
    color:#f47500
}
 #tocify li a:hover{
    color:#f47500;
    text-decoration:underline
}
 .post-body .contact-form{
    display:table;
}
 .contact-form .widget-title{
    display:none
}
 .contact-form .contact-form-name{
    width:calc(50% - 5px)
}
 .contact-form .contact-form-email{
    float:right;
    width:calc(50% - 5px)
}
 .post-body pre,pre.code-box{
    position:relative;
    display:block;
    background-color:rgba(155,155,155,0.05);
    font-family:Monospace;
    font-size:13px;
    color:#47474a;
    white-space:pre-wrap;
    line-height:1.4em;
    padding:15px;
    margin:0;
    border:1px solid rgba(155,155,155,0.1);
    border-radius:3px
}
  .is-dark .post-body pre, .is-dark pre.code-box {
  color:#a1a1a1;
  }
 .post-body .google-auto-placed{
    margin:25px 0
}
  #hidden-widgets-wrap,.hidden-widgets{
    display:none;
    visibility:hidden
}
  @media only screen and (max-width: 680px) {
.post-body table {
    display: block;
}
  }
</style>
    </b:if>
<b:if cond='data:view.isLayoutMode'>
<b:template-skin>
<![CDATA[
/*------Layout (No Edit)----------*/
body#layout{width:800px;}
body#layout #outer-wrapper,body#layout .row{width:auto;padding:0}
body#layout{width:800px;position:relative;padding:95px 5px 0;margin:0}
body#layout div.section{margin:0 5px 10px!important;padding:16px 16px 18px!important}
body#layout .section h4{font-size:14px;margin:0}
body#layout .layout-widget-description{display:none}
body#layout .theme-options,body#layout #main-menu .widget{display:block!important}
body#layout div.sora-panel{background-color:#d7d7d7!important;overflow:hidden!important;border-color:#bcbcbc}
body#layout .header-header .flex-left .top-bar-nav, body#layout .header-header .flex-right .top-bar-social, body#layout .header-header .flex-center .header-logo {
    width: 100%;
}
body#layout .header-header .flex-left .section, body#layout .header-header .flex-right .section {
    width: 100%;
}
body#layout .header-header .flex-left, body#layout .header-header .flex-right, body#layout .header-header .flex-center {
    display: flex;
    width: 100%;
}
body#layout .mobile-search, body#layout .tgl-wrap {
    display: none;
}
body#layout #header-wrap{height:auto}
body#layout .header-header{float:left;width:100%;height:auto;padding:0}
body#layout .header-header .container{
    display: flex;}
body#layout .header-menu{float:left;width:100%;height:auto}
body#layout #main-menu{height:auto}
body#layout #hot-wrapper .widget{display:block}
body#layout #content-wrapper{margin:0}
body#layout #content-wrapper > .container{display:flex;margin:0}
body#layout #main-wrapper{width:66.66%;padding:0}
body#layout #sidebar-wrapper{width:33.33%;padding:0}
body#layout .sidebar .widget,body#layout .sidebar .widget-content{float:none;overflow:visible}
body#layout .footer-widgets-wrap{display:flex}
body#layout .footer-widgets-wrap div.footer{width:100%}
body#layout .top-bar {
    height: auto;
}
body#layout #hidden-widgets{
    display:none!important
}

/*------Layout (end)----------*/
]]></b:template-skin>
</b:if>

<!-- Global Variables -->
<script type='text/javascript'>
//<![CDATA[
// Global variables with content. "Available for Edit"
var monthFormat = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    noThumbnail = "https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png",
    postPerPage = 7,
    fixedSidebar = true,
    commentsSystem = "blogger",
    disqusShortname = "soratemplates";
//]]>
</script>

<b:defaultmarkups>
  <b:defaultmarkup type='Common'>
    <b:includable id='widget-title'>
      <b:if cond='data:defaultTitle or data:title'>
        <div class='widget-title'>
          <h3 class='title'>
            <data:title/>
          </h3>
        </div>
      </b:if>
    </b:includable>
    <b:includable id='contact-form-content'>
      <div class='widget-content contact-form-widget'>
        <div class='form'>
          <form name='contact-form'>
            <input class='contact-form-name' expr:ariby='data:contactFormNameMsg' expr:id='data:widget.instanceId + &quot;_contact-form-name&quot;' expr:placeholder='data:contactFormNameMsg' name='name' size='30' type='text' value=''/>
            <input class='contact-form-email' expr:ariby='data:contactFormEmailMsg + &quot; *&quot;' expr:id='data:widget.instanceId + &quot;_contact-form-email&quot;' expr:placeholder='data:contactFormEmailMsg + &quot; *&quot;' name='email' size='30' type='text' value=''/>
            <textarea class='contact-form-email-message' cols='25' expr:ariby='data:contactFormMessageMsg + &quot; *&quot;' expr:id='data:widget.instanceId + &quot;_contact-form-email-message&quot;' expr:placeholder='data:contactFormMessageMsg + &quot; *&quot;' name='email-message' rows='5'/>
            <input class='contact-form-button btn contact-form-button-submit' expr:id='data:widget.instanceId + &quot;_contact-form-submit&quot;' expr:value='data:contactFormSendMsg' type='button'/>
            <p class='contact-form-error-message' expr:id='data:widget.instanceId + &quot;_contact-form-error-message&quot;'/>
            <p class='contact-form-success-message' expr:id='data:widget.instanceId + &quot;_contact-form-success-message&quot;'/>
          </form>
        </div>
      </div>
    </b:includable>
    <b:includable id='theme-head'>
    <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1' name='viewport'/>
    <title><data:view.title.escaped/></title>
<link href='//1.bp.blogspot.com' rel='dns-prefetch'/>
    <link href='//2.bp.blogspot.com' rel='dns-prefetch'/>
    <link href='//3.bp.blogspot.com' rel='dns-prefetch'/>
    <link href='//4.bp.blogspot.com' rel='dns-prefetch'/>
    <link href='//www.blogger.com' rel='dns-prefetch'/>
    <link href='//dnjs.cloudflare.com' rel='dns-prefetch'/>
    <link href='//fonts.gstatic.com' rel='dns-prefetch'/>
    <link href='//pagead2.googlesyndication.com' rel='dns-prefetch'/>
    <link href='//www.googletagmanager.com' rel='dns-prefetch'/>
    <link href='//www.google-analytics.com' rel='dns-prefetch'/>
    <link href='//connect.facebook.net' rel='dns-prefetch'/>
    <link href='//c.disquscdn.com' rel='dns-prefetch'/>
    <link href='//disqus.com' rel='dns-prefetch'/>
      <meta expr:content='&quot;text/html; charset=&quot; + data:blog.encoding' http-equiv='Content-Type'/>
      <meta content='blogger' name='generator'/>
      <link expr:href='data:blog.blogspotFaviconUrl' rel='icon' type='image/x-icon'/>
      <meta expr:content='data:skin.vars.keycolor' name='theme-color'/>
      <meta expr:content='data:skin.vars.keycolor' name='msapplication-navbutton-color'/>
      <b:if cond='data:blog.adultContent'>
        <meta content='adult' name='rating'/>
      </b:if>
      <link expr:href='data:view.url.canonical' rel='canonical'/>
      <data:blog.feedLinks/><data:blog.meTag/>
      <meta expr:content='data:view.description.escaped' name='description'/>
      <b:tag cond='data:view.isMultipleItems and data:widgets.Blog.first.posts[0].featuredImage' expr:href='data:widgets.Blog.first.posts[0].featuredImage' name='link' rel='image_src'/>
      <b:tag cond='data:view.isSingleItem and data:view.featuredImage' expr:href='data:view.featuredImage' name='link' rel='image_src'/>
      <b:include name='customOpenGraphMetaData'/>
    </b:includable> 
  <b:includable id='customOpenGraphMetaData'>
      <!-- Metadata for Open Graph protocol. See http://ogp.me/. -->
      <b:if cond='data:view.isHomepage'>
        <meta content='website' property='og:type'/>
      </b:if>
      <b:if cond='data:view.isSingleItem'>
        <meta content='article' property='og:type'/>
      </b:if>
      <b:if cond='data:view.isMultipleItems and not data:view.isHomepage'>
        <meta content='object' property='og:type'/>
      </b:if>    
      <meta expr:content='data:view.title.escaped' property='og:title'/>
      <meta expr:content='data:blog.url.canonical' property='og:url'/>
      <meta expr:content='data:view.description.escaped' property='og:description'/>
      <meta expr:content='data:blog.title.escaped' property='og:site_name'/>
      <b:tag cond='data:view.isMultipleItems and data:widgets.Blog.first.posts[0].featuredImage' expr:content='data:widgets.Blog.first.posts[0].featuredImage' name='meta' property='og:image'/>
      <b:if cond='data:view.featuredImage'>
        <meta expr:content='data:view.featuredImage' property='og:image'/>
        <meta expr:content='data:view.featuredImage' name='twitter:image'/>
      </b:if>
      <meta content='summary_large_image' name='twitter:card'/>
      <meta expr:content='data:view.title.escaped' name='twitter:title'/>
      <meta expr:content='data:blog.url.canonical' name='twitter:domain'/>
      <meta expr:content='data:view.description.escaped' name='twitter:description'/>
      <b:if cond='data:view.isHomepage'>
        <script type='application/ld+json'>{&quot;@context&quot;:&quot;http://schema.org&quot;,&quot;@type&quot;:&quot;WebSite&quot;,&quot;name&quot;:&quot;<data:view.title.escaped/>&quot;,&quot;url&quot;:&quot;<data:view.url.canonical/>&quot;,&quot;potentialAction&quot;:{&quot;@type&quot;:&quot;SearchAction&quot;,&quot;target&quot;:&quot;<data:view.url.canonical/>search?q={search_term_string}&quot;,&quot;query-input&quot;:&quot;required name=search_term_string&quot;}}</script>
      </b:if>
    </b:includable>  
    <b:includable id='translate'>
      <b:switch var='data:blog.locale.language'>
        <b:case value='en'/><b:include name='customLang'/>
        <b:default/><b:include name='customLang'/>
      </b:switch>
    </b:includable> 
   <b:includable id='customLang'>
    <b:switch var='data:message'>
        <b:case value='prevPost'/>
        <b:if cond='data:blog.locale.language == &quot;en&quot;'>Previous Post<b:else/><data:messages.newer/></b:if>
        <b:case value='nextPost'/>
        <b:if cond='data:blog.locale.language == &quot;en&quot;'>Next Post<b:else/><data:messages.older/></b:if>
        <b:case value='loadMorePosts'/>
        <b:if cond='data:blog.locale.language == &quot;en&quot;'>Load More<b:else/><data:messages.loadMorePosts/></b:if>
        <b:case value='noMorePosts'/>
        <b:if cond='data:blog.locale.language == &quot;en&quot;'>That is All<b:else/><data:messages.noResultsFound/></b:if>
    </b:switch>
</b:includable>   
  </b:defaultmarkup>
  
  <b:defaultmarkup type='PopularPosts'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
          <b:tag class='main-slider' cond='data:widget.sectionId == &quot;slider-section&quot;' name='ul'>
        <b:loop index='i' values='data:posts' var='post'>
          <b:include data='post' name='postContent'/>
        </b:loop>
            </b:tag>
      </div>
    </b:includable>
    <b:includable id='postContent' var='post'>
       <b:if cond='data:widget.sectionId == &quot;slider-section&quot;'>
        <b:include data='post' name='slider-section'/>
        <b:else/>
        <b:include data='post' name='default'/>
      </b:if>
    </b:includable>
     <b:includable id='slider-section' var='post'>
         <b:if cond='data:i lt 10'>
           <li class='slider-item'>
              <b:class expr:name='&quot;item-&quot;+data:i'/>
               <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
          </a>
              <div class='post-info-wrap'><div class='post-info'>
              <b:if cond='data:post.labels'><span class='post-tag'><data:post.labels.first.name/></span></b:if>
               <h2 class='post-title'>
               <a expr:href='data:post.url'><data:post.title/></a>
               </h2>
               </div></div>
           </li>
           </b:if>
       </b:includable>
    <b:includable id='default' var='post'>
       <div class='post default-popularpost'>  
              <b:class expr:name='&quot;item-&quot;+data:i'/>
        <div class='post-content'>
          <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
          </a>
          <div class='post-info'>
            <h2 class='post-title'>
              <a expr:href='data:post.url'><data:post.title/></a>
            </h2>
            <div class='post-meta'>
              <span class='post-date published' expr:datetime='data:post.date.iso8601'><data:post.date/></span>
            </div>
          </div>
        </div>
      </div>
    </b:includable>  
  </b:defaultmarkup>
  <b:defaultmarkup type='Header'>
    <b:includable id='main' var='this'>
      <div class='header-widget'>
        <b:include cond='data:imagePlacement in {&quot;REPLACE&quot;, &quot;BEFORE_DESCRIPTION&quot;}' name='image'/>
        <b:include cond='data:imagePlacement == &quot;BEHIND&quot;' name='title'/>
      </div>
    </b:includable>
    <b:includable id='image'>
      <a class='header-image-wrapper' expr:href='data:blog.homepageUrl'>
        <img expr:alt='data:blog.title.escaped' expr:data-height='data:height' expr:data-width='data:width' expr:src='data:image'/>
      </a>
    </b:includable>
  </b:defaultmarkup>
  <b:defaultmarkup type='FeaturedPost'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
        <b:loop values='data:posts' var='post'>
          <b:include data='post' name='postContent'/>
        </b:loop>
      </div>
    </b:includable>
    <b:includable id='postContent' var='post'>
      <div class='post'>
        <div class='post-content'>
          <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
            <span class='post-tag'><data:post.labels.last.name/></span>
          </a>
          <div class='post-info'>
            <h2 class='post-title'>
              <a expr:href='data:post.url'><data:post.title/></a>
            </h2>
            <div class='post-meta'>
              <span class='post-date published' expr:datetime='data:post.date.iso8601'><data:post.date/></span>
            </div>
          </div>
        </div>
      </div>
    </b:includable>
  </b:defaultmarkup>
  <b:defaultmarkup type='ContactForm'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
    <b:includable id='content'>
      <b:include name='contact-form-content'/>
    </b:includable>       
  </b:defaultmarkup>
  <b:defaultmarkup type='Label'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content'>
        <b:class expr:name='data:this.display + &quot;-label&quot;'/>
        <b:include cond='data:this.display == &quot;list&quot;' name='list'/>
        <b:include cond='data:this.display == &quot;cloud&quot;' name='list'/>
      </div>
    </b:includable>
    <b:includable id='list'>
      <ul>
        <b:loop values='data:labels' var='label'>
          <li>
            <a class='label-name' expr:href='data:label.url'>
              <data:label.name/>
              <b:if cond='data:this.showFreqNumbers'>
                <span class='label-count'><data:label.count/></span>
              </b:if>
            </a>
          </li>
        </b:loop>
      </ul>
    </b:includable>
  </b:defaultmarkup>
  <b:defaultmarkup type='FollowByEmail'>
    <b:includable id='main' var='this'>
      <b:include name='content'/>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content'>
        <b:if cond='data:defaultTitle or data:title'>
          <h3 class='title'>
            <data:title/>
          </h3>
        </b:if>
        <span class='before-text'><data:skin.vars.followByEmail/></span>
        <div class='follow-by-email-inner'>
          <form action='https://feedburner.google.com/fb/a/mailverify' expr:onsubmit='&quot;window.open(\&quot;https://feedburner.google.com/fb/a/mailverify?uri=&quot; + data:feedPath + &quot;\&quot;, \&quot;popupwindow\&quot;, \&quot;scrollbars=yes,width=550,height=520\&quot;); return true&quot;' method='post' target='popupwindow'>
            <input autocomplete='off' class='follow-by-email-address' expr:placeholder='data:messages.emailAddress' name='email' type='email'/>
            <input class='follow-by-email-submit' expr:value='data:messages.subscribe' type='submit'/>
            <input expr:value='data:feedPath' name='uri' type='hidden'/>
            <input name='loc' type='hidden' value='en_US'/>
          </form>
        </div>
      </div>
    </b:includable>
  </b:defaultmarkup>
  <b:defaultmarkup type='BlogSearch'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content' role='search'>
        <form class='search-form' expr:action='data:blog.searchUrl'>
          <b:attr cond='not data:view.isPreview' name='target' value='_top'/>
          <b:include name='urlParamsAsFormInput'/>
          <input autocomplete='off' class='search-input' expr:aria-label='data:messages.searchThisBlog' expr:placeholder='data:messages.searchThisBlog' expr:value='data:view.isSearch ? data:view.search.query.escaped : &quot;&quot;' name='q'/>
          <input class='search-action' expr:value='data:messages.search.escaped' type='submit'/>  
        </form>
      </div>
    </b:includable>
  </b:defaultmarkup>
  <b:defaultmarkup type='BlogArchive'>
    <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content'>
        <div id='ArchiveList'>
          <div expr:id='data:widget.instanceId + &quot;_ArchiveList&quot;'>
            <b:include cond='data:this.style in {&quot;FLAT&quot;, &quot;MENU&quot;, &quot;HIERARCHY&quot;}' name='flat'/>
          </div>
        </div>
      </div>
    </b:includable>
    <b:includable id='flat'>
      <ul class='flat'>
        <b:loop values='data:data' var='i'>
          <li class='archivedate'>
            <a expr:href='data:i.url'>
              <data:i.name/><span class='post-count'><data:i.post-count/></span>
            </a>
          </li>
        </b:loop>
      </ul>
    </b:includable>
  </b:defaultmarkup>
</b:defaultmarkups>

    <!-- Google Analytics -->
    <b:include data='blog' name='google-analytics'/>

</head>
<body expr:class='data:blog.pageType'>
  <b:class cond='data:view.isHomepage' name='home'/>
  <b:class cond='data:view.isPage' name='item'/>
  <b:class cond='data:view.isArchive' name='index'/>
  <b:class cond='data:view.isError' name='error404'/>

<!-- Theme Options -->
  <div class='theme-options' style='display:none'>
    <b:section class='sora-panel' id='sora-panel' maxwidgets='1' name='Theme Options' showaddelement='no'>
      <b:widget id='LinkList71' locked='true' title='Default Variables' type='LinkList' version='2' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='link-3'>6</b:widget-setting>
          <b:widget-setting name='sorting'>NONE</b:widget-setting>
          <b:widget-setting name='text-1'>commentsSystem</b:widget-setting>
          <b:widget-setting name='link-1'>blogger</b:widget-setting>
          <b:widget-setting name='text-0'>disqusShortname</b:widget-setting>
          <b:widget-setting name='link-2'>true</b:widget-setting>
          <b:widget-setting name='text-3'>postPerPage</b:widget-setting>
          <b:widget-setting name='link-0'>soratemplates</b:widget-setting>
          <b:widget-setting name='text-2'>fixedSidebar</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
          <b:include name='content'/>
        </b:includable>
        <b:includable id='content'>
          &lt;script type=&#39;text/javascript&#39;&gt;
          //&lt;![CDATA[
          <b:loop values='data:links' var='link'>
            <b:if cond='data:link.name == &quot;postPerPage&quot;'>
              var postPerPage = <data:link.target/>;
            </b:if>
            <b:if cond='data:link.name == &quot;fixedSidebar&quot;'>
              var fixedSidebar = <data:link.target/>;
            </b:if>
            <b:if cond='data:link.name == &quot;commentsSystem&quot;'>
              var commentsSystem = &quot;<data:link.target/>&quot;;
            </b:if>
            <b:if cond='data:link.name == &quot;disqusShortname&quot;'>
              var disqusShortname = &quot;<data:link.target/>&quot;;
            </b:if>
          </b:loop>
          //]]&gt;
          &lt;/script&gt;
        </b:includable>
      </b:widget>
    </b:section>
  </div>
  
 <div class='mobile-side-menu' id='hide-them-menu'>
<div class='slide-menu-header'>
   <div class='flex-content flex-center'>
          <b:section class='header-logo' id='header-logo' maxwidgets='1' name='Header Logo' showaddelement='yes'>
            <b:widget id='Header1' locked='true' title='WHO CX Platform (Header)' type='Header' version='2' visible='true'>
              <b:widget-settings>
                <b:widget-setting name='displayUrl'/>
                <b:widget-setting name='displayHeight'>0</b:widget-setting>
                <b:widget-setting name='sectionWidth'>150</b:widget-setting>
                <b:widget-setting name='useImage'>false</b:widget-setting>
                <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
                <b:widget-setting name='imagePlacement'>BEHIND</b:widget-setting>
                <b:widget-setting name='displayWidth'>0</b:widget-setting>
              </b:widget-settings>
              <b:includable id='main' var='this'>
      <div class='header-widget'>
        <b:include cond='data:imagePlacement in {&quot;REPLACE&quot;, &quot;BEFORE_DESCRIPTION&quot;}' name='image'/>
        <b:include cond='data:imagePlacement == &quot;BEHIND&quot;' name='title'/>
      </div>
    </b:includable>
              <b:includable id='behindImageStyle'>
    <b:if cond='data:sourceUrl'>
      <b:include cond='data:this.image' data='{                    image: data:this.image,                    selector: &quot;.header-widget&quot;                  }' name='responsiveImageStyle'/>
      <style type='text/css'>
        .header-widget {
          background-position: <data:blog.locale.languageAlignment/>;
          background-repeat: no-repeat;
        }
      </style>
    </b:if>
  </b:includable>
              <b:includable id='description'>
    <p>
      <data:this.description/>
    </p>
  </b:includable>
              <b:includable id='image'>
      <a class='header-image-wrapper' expr:href='data:blog.homepageUrl'>
        <img expr:alt='data:blog.title.escaped' expr:data-height='data:height' expr:data-width='data:width' expr:src='data:image'/>
      </a>
    </b:includable>
              <b:includable id='title'>
    <h1>
      <b:tag cond='data:view.url != data:blog.homepageUrl' expr:href='data:blog.homepageUrl' name='a'>
        <data:title/>
      </b:tag>
    </h1>
  </b:includable>
            </b:widget>
          </b:section>
        </div>
    <a class='hide-freepic-pro-mobile-menu' href='javascript:;' role='button'/>
  </div>
     <div class='slide-menu-flex'>
     <div class='mobile-menu-wrap' id='mobile-menu-wrap'>
      <div class='mobile-menu'>      
        <b:section class='main-menu' id='main-menu' maxwidgets='1' name='Main Menu' showaddelement='yes'>
                <b:widget id='LinkList74' locked='true' title='Review Categories' type='LinkList' version='2' visible='true'>
                  <b:widget-settings>
                    <b:widget-setting name='text-10'><![CDATA[<i class="ri-stack-line"></i>Features]]></b:widget-setting>
                    <b:widget-setting name='shownum'>10</b:widget-setting>
                    <b:widget-setting name='sorting'>NONE</b:widget-setting>
                    <b:widget-setting name='link-1'>/</b:widget-setting>
                    <b:widget-setting name='link-2'>/</b:widget-setting>
                    <b:widget-setting name='link-12'>https://www.whocx.com</b:widget-setting>
                    <b:widget-setting name='link-0'>#</b:widget-setting>
                    <b:widget-setting name='link-11'>#</b:widget-setting>
                    <b:widget-setting name='link-10'>#</b:widget-setting>
                    <b:widget-setting name='text-9'>_Health Leaders Review </b:widget-setting>
                    <b:widget-setting name='link-9'>/</b:widget-setting>
                    <b:widget-setting name='text-8'>_Health Organizations Review </b:widget-setting>
                    <b:widget-setting name='link-7'>#</b:widget-setting>
                    <b:widget-setting name='link-8'>#</b:widget-setting>
                    <b:widget-setting name='link-5'>#</b:widget-setting>
                    <b:widget-setting name='link-6'>#</b:widget-setting>
                    <b:widget-setting name='link-3'>https://www.whocx.com/2023/02/top-10-public-health-courses-on.html</b:widget-setting>
                    <b:widget-setting name='link-4'>#</b:widget-setting>
                    <b:widget-setting name='text-1'>_Health Articles Review</b:widget-setting>
                    <b:widget-setting name='text-0'>Health Education</b:widget-setting>
                    <b:widget-setting name='text-3'>_Health Courses Review</b:widget-setting>
                    <b:widget-setting name='text-2'>_Health Books Review </b:widget-setting>
                    <b:widget-setting name='text-5'>_Health Softwares Review </b:widget-setting>
                    <b:widget-setting name='text-4'>Health Products</b:widget-setting>
                    <b:widget-setting name='text-7'>Health Resources</b:widget-setting>
                    <b:widget-setting name='text-6'>_Health Wearable Devices Review </b:widget-setting>
                    <b:widget-setting name='text-11'><![CDATA[<i class="ri-code-box-line"></i>Documentation]]></b:widget-setting>
                    <b:widget-setting name='text-12'><![CDATA[<i class="ri-file-download-line"></i>Download This Template]]></b:widget-setting>
                  </b:widget-settings>
                  <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
                  <b:includable id='content'>
              <ul id='main-menu-nav' role='menubar'>
                <b:loop values='data:links' var='link'>
                  <li><a expr:href='data:link.target' role='menuitem'><data:link.name/></a></li>
                </b:loop>
              </ul>
            </b:includable>
                </b:widget>
              </b:section>
        <div class='clearfix'/>
         <b:section class='side-bar-nav' id='side-bar-nav' maxwidgets='3' name='Extra Menu' showaddelement='yes'>
           <b:widget id='LinkList38' locked='true' title='Link List' type='LinkList' version='2' visible='false'>
             <b:widget-settings>
               <b:widget-setting name='sorting'>NONE</b:widget-setting>
               <b:widget-setting name='text-1'><![CDATA[<i class="ri-pantone-line"></i>Custom Menu 02]]></b:widget-setting>
               <b:widget-setting name='link-1'>/</b:widget-setting>
               <b:widget-setting name='text-0'><![CDATA[<i class="ri-pantone-fill"></i>Custom Menu 01]]></b:widget-setting>
               <b:widget-setting name='link-0'>/</b:widget-setting>
             </b:widget-settings>
             <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
             <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul> 
              </div>
            </b:includable>
           </b:widget>
           <b:widget id='LinkList36' locked='true' title='Link List' type='LinkList' version='2' visible='false'>
             <b:widget-settings>
               <b:widget-setting name='sorting'>NONE</b:widget-setting>
               <b:widget-setting name='text-1'><![CDATA[<i class="ri-external-link-line"></i>Normal Link 02]]></b:widget-setting>
               <b:widget-setting name='link-1'>/</b:widget-setting>
               <b:widget-setting name='text-0'><![CDATA[<i class="ri-external-link-line"></i>Normal Link 01]]></b:widget-setting>
               <b:widget-setting name='link-0'>/</b:widget-setting>
             </b:widget-settings>
             <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
             <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul> 
              </div>
            </b:includable>
           </b:widget>
           <b:widget id='LinkList37' locked='true' title='Link List' type='LinkList' version='2' visible='false'>
             <b:widget-settings>
               <b:widget-setting name='sorting'>NONE</b:widget-setting>
               <b:widget-setting name='text-1'><![CDATA[<i class="ri-edit-box-line"></i>Terms]]></b:widget-setting>
               <b:widget-setting name='link-1'>https://whocx.com</b:widget-setting>
               <b:widget-setting name='text-0'><![CDATA[<i class="ri-profile-line"></i>Disclaimer]]></b:widget-setting>
               <b:widget-setting name='link-2'>https://whocx.com</b:widget-setting>
               <b:widget-setting name='link-0'>https://whocx.com</b:widget-setting>
               <b:widget-setting name='text-2'><![CDATA[<i class="ri-file-text-line"></i>Policy]]></b:widget-setting>
             </b:widget-settings>
             <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
             <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul> 
              </div>
            </b:includable>
           </b:widget>
         </b:section>
       </div>
    </div>
    <div class='mm-footer'>
      <div class='mm-social'>
          <!-- Top Social --> 
        <b:section class='top-bar-social social' id='top-bar-social' maxwidgets='1' name='Social Side' showaddelement='yes'>
           <b:widget id='LinkList73' locked='true' title='Social Widget' type='LinkList' version='2' visible='false'>
             <b:widget-settings>
               <b:widget-setting name='link-3'>#</b:widget-setting>
               <b:widget-setting name='sorting'>NONE</b:widget-setting>
               <b:widget-setting name='text-1'>twitter</b:widget-setting>
               <b:widget-setting name='link-1'>https://twitter.com/phidevs</b:widget-setting>
               <b:widget-setting name='text-0'>facebook</b:widget-setting>
               <b:widget-setting name='link-2'>https://www.instagram.com/phidevs/</b:widget-setting>
               <b:widget-setting name='text-3'>pinterest</b:widget-setting>
               <b:widget-setting name='link-0'>https://www.facebook.com/phidevs/</b:widget-setting>
               <b:widget-setting name='text-2'>instagram</b:widget-setting>
             </b:widget-settings>
             <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
             <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li expr:class='data:link.name'><a expr:href='data:link.target' expr:title='data:link.name' target='_blank'/></li>
                  </b:loop>
                </ul>
              </div>
            </b:includable>
           </b:widget>
         </b:section>
      </div>
      <div class='mm-menu'/>
    </div>
    </div>
</div>
<!-- Outer Wrapper -->
<div id='outer-wrapper'>
   <!-- Header Wrapper -->
  <div id='header-wrap'>
    <div class='header-header flex-content'>    
      <div class='container row'>
    <div class='flex-left flex-content'>       
        <span class='mobile-menu-toggle'/>
        <b:section class='mobile-logo' id='mobile-logo' maxwidgets='1' name='Mobile Logo' showaddelement='yes'>
          <b:widget id='Image70' locked='true' title='Mobile Logo Settings' type='Image' version='2' visible='false'>
            <b:widget-settings>
              <b:widget-setting name='displayUrl'>https://blogger.googleusercontent.com/img/a/AVvXsEjZum3OXC0bt6nLCVBJRvP45V08m8shJ8pEQsY2GEDUedF0WHaweM4ZaNLVs1kM3W7kldfuZMWQy0WcUpgTkGtTq7m9toZGDM_eI-hVI5eIeh1blKFEb65Zn9nJeIBI1fDcs67gh2zYfUeg12Q1-BPAHddfFe0Y1gbojXGf-Mo7jB-dxZB8eljhTMg=s1600</b:widget-setting>
              <b:widget-setting name='displayHeight'>1600</b:widget-setting>
              <b:widget-setting name='sectionWidth'>150</b:widget-setting>
              <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
              <b:widget-setting name='displayWidth'>1600</b:widget-setting>
              <b:widget-setting name='link'>My Title</b:widget-setting>
              <b:widget-setting name='caption'>image</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
            <b:include name='content'/>
          </b:includable>
            <b:includable id='content'>
            <div class='logo-content'>
              <b:if cond='data:caption == &quot;image&quot;'>
                <a expr:href='data:blog.homepageUrl'><img expr:alt='data:blog.title' expr:src='data:sourceUrl'/></a>
                <b:elseif cond='data:caption == &quot;custom&quot;'/>
                <b:if cond='data:link'>
                  <h3><a expr:href='data:blog.homepageUrl'><data:link/></a></h3>
                </b:if>
                <b:else/>   
                <h3><a expr:href='data:blog.homepageUrl'><data:blog.title/></a></h3>       
              </b:if> 
            </div>
          </b:includable>
          </b:widget>
        </b:section>
        <div class='mobile-search'>
      <form class='search-form' expr:action='data:blog.searchUrl' role='search'>
        <input autocomplete='off' class='search-input' expr:placeholder='data:messages.search' name='q' type='search' value=''/>
        <button class='search-action' type='submit' value=''/>
      </form>
    </div>
         <div class='tgl-wrap'>
           <a class='darkmode-toggle' href='javascript:;' role='button'><i/></a>
</div>
        <span class='search-menu-toggle'/>
        </div>
        <div class='flex-right flex-content'> 
    <b:section class='top-bar-nav' id='top-bar-nav' maxwidgets='1' name='Top Navigation' showaddelement='yes'>
       <b:widget id='LinkList72' locked='true' title='Link List' type='LinkList' version='2' visible='true'>
         <b:widget-settings>
           <b:widget-setting name='sorting'>NONE</b:widget-setting>
           <b:widget-setting name='text-1'><![CDATA[<i class="ri-file-user-line"></i>About]]></b:widget-setting>
           <b:widget-setting name='link-1'>https://whocx.com</b:widget-setting>
           <b:widget-setting name='text-0'><![CDATA[<i class="ri-home-8-line"></i>Home]]></b:widget-setting>
           <b:widget-setting name='link-2'>https://whocx.com</b:widget-setting>
           <b:widget-setting name='link-0'>/</b:widget-setting>
           <b:widget-setting name='text-2'><![CDATA[<i class="ri-phone-line"></i>Contact]]></b:widget-setting>
         </b:widget-settings>
         <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
         <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul> 
              </div>
            </b:includable>
       </b:widget>
     </b:section>
        </div>
      </div>
    </div>

  </div>

  <div class='clearfix'/>
<div id='overlap-wrapper'>
<b:section class='row home-ad' id='home-ad' maxwidgets='1' name='Home Ads' showaddelement='yes'>
  <b:widget id='HTML33' locked='false' title='Advertisement' type='HTML' version='2' visible='false'>
    <b:widget-settings>
      <b:widget-setting name='content'>&lt;a class=&quot;sora-ads-full&quot; href=&quot;javascript:;&quot;&gt;Responsive Advertisement&lt;/a&gt;
&lt;style&gt;
.sora-ads-full {
 display: block;
    background-color: rgb(0 0 0 / 10%);
    text-align: center;
    font-size: 13px;
    color: #aaaaaa;
    font-weight: 400;
    font-style: italic;
    line-height: 88px;
    border: 1px solid rgb(0 0 0 / 10%);
}
&lt;/style&gt;</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
                <b:include name='widget-title'/>
                <div class='widget-content'>
                  <data:content/>
                </div>
              </b:includable>
  </b:widget>
</b:section>
 <div class='clearfix'/>
  <!-- Content Wrapper -->
  <div class='row' id='content-wrapper'>
    <div class='container'>

      <!-- Main Wrapper -->
      <div id='main-wrapper'>
        <b:if cond='data:view.isHomepage'> 
    <div id='main-feat-wrapper'>
      <b:section id='featured-section' maxwidgets='1' name='Featured Posts' showaddelement='yes'>
        <b:widget id='FeaturedPost1' locked='false' title='Featured post' type='FeaturedPost' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='showSnippet'>true</b:widget-setting>
            <b:widget-setting name='showPostTitle'>true</b:widget-setting>
            <b:widget-setting name='postId'>6321927076501888089</b:widget-setting>
            <b:widget-setting name='showFirstImage'>true</b:widget-setting>
            <b:widget-setting name='useMostRecentPost'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
        <b:loop values='data:posts' var='post'>
          <b:include data='post' name='postContent'/>
        </b:loop>
      </div>
    </b:includable>
          <b:includable id='blogThisShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=270,width=475\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
          <b:includable id='bylineByName' var='byline'>
  <b:switch var='data:byline.name'>
  <b:case value='share'/>
    <b:include cond='data:post.shareUrl' name='postShareButtons'/>
  <b:case value='comments'/>
    <b:include cond='data:post.allowComments' name='postCommentsLink'/>
  <b:case value='location'/>
    <b:include cond='data:post.location' name='postLocation'/>
  <b:case value='timestamp'/>
    <b:include cond='not data:view.isPage' name='postTimestamp'/>
  <b:case value='author'/>
    <b:include name='postAuthor'/>
  <b:case value='labels'/>
    <b:include cond='data:post.labels' name='postLabels'/>
  <b:case value='icons'/>
    <b:include cond='data:post.emailPostUrl' name='emailPostIcon'/>
  </b:switch>
</b:includable>
          <b:includable id='bylineRegion' var='regionItems'>
  <b:loop values='data:regionItems' var='byline'>
    <b:include data='byline' name='bylineByName'/>
  </b:loop>
</b:includable>
          <b:includable id='commentsLink'>
  <a class='comment-link' expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
    <b:if cond='data:post.numberOfComments &gt; 0'>
      <b:message name='messages.numberOfComments'>
        <b:param expr:value='data:post.numberOfComments' name='numComments'/>
      </b:message>
    <b:else/>
      <data:messages.postAComment/>
    </b:if>
  </a>
</b:includable>
          <b:includable id='commentsLinkIframe'>
  <!-- G+ comments, no longer available. The includable is retained for backwards-compatibility. -->
</b:includable>
          <b:includable id='emailPostIcon'>
  <span class='byline post-icons'>
    <!-- email post links -->
    <span class='item-action'>
      <a expr:href='data:post.emailPostUrl' expr:title='data:messages.emailPost'>
        <b:include data='{ iconClass: &quot;touch-icon sharing-icon&quot; }' name='emailIcon'/>
      </a>
    </span>
  </span>
</b:includable>
          <b:includable id='facebookShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=430,width=640\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
          <b:includable id='footerBylines'>
  <b:if cond='data:widgets.Blog.first.footerBylines'>
    <b:loop index='i' values='data:widgets.Blog.first.footerBylines' var='region'>
      <b:if cond='not data:region.items.empty'>
        <div expr:class='&quot;post-footer-line post-footer-line-&quot; + (data:i + 1)'>
          <b:with value='&quot;footer-&quot; + (data:i + 1)' var='regionName'>
            <b:include data='region.items' name='bylineRegion'/>
          </b:with>
        </div>
      </b:if>
    </b:loop>
  </b:if>
</b:includable>
          <b:includable id='googlePlusShare'>
  <div class='goog-inline-block google-plus-share-container'>
    <g:plusone annotation='inline' expr:href='data:originalUrl.canonical.http' size='medium' source='blogger:blog:plusone'/>
  </div>
</b:includable>
          <b:includable id='headerByline'>
  <b:if cond='data:widgets.Blog.first.headerByline'>
    <div class='post-header'>
      <div class='post-header-line-1'>
        <b:with value='&quot;header-1&quot;' var='regionName'>
          <b:include data='data:widgets.Blog.first.headerByline.items' name='bylineRegion'/>
        </b:with>
      </div>
    </div>
  </b:if>
</b:includable>
          <b:includable id='linkShare'>
  <b:with value='&quot;window.prompt(\&quot;Copy to clipboard: Ctrl+C, Enter\&quot;, \&quot;&quot; + data:originalUrl + &quot;\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
          <b:includable id='otherSharingButton'>
  <span class='sharing-platform-button sharing-element-other' expr:aria-label='data:messages.shareToOtherApps.escaped' expr:data-url='data:originalUrl' expr:title='data:messages.shareToOtherApps.escaped' role='menuitem' tabindex='-1'>
    <b:with value='{key: &quot;sharingOther&quot;}' var='platform'>
      <b:include name='sharingPlatformIcon'/>
    </b:with>
    <span class='platform-sharing-text'><data:messages.shareOtherApps.escaped/></span>
  </span>
</b:includable>
          <b:includable id='platformShare'>
  <a expr:class='&quot;goog-inline-block sharing-&quot; + data:platform.key' expr:data-url='data:originalUrl' expr:href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:onclick='data:onclick ? data:onclick : &quot;&quot;' expr:title='data:platform.shareMessage' target='_blank'>
    <span class='share-button-link-text'>
      <data:platform.shareMessage/>
    </span>
  </a>
</b:includable>
          <b:includable id='postAuthor'>
  <span class='byline post-author vcard'>
    <span class='post-author-label'>
      <data:byline.label/>
    </span>
    <span class='fn'>
      <b:if cond='data:post.author.profileUrl'>
        <meta expr:content='data:post.author.profileUrl'/>
        <a class='g-profile' expr:href='data:post.author.profileUrl' rel='author' title='author profile'>
          <span><data:post.author.name/></span>
        </a>
      <b:else/>
        <span><data:post.author.name/></span>
      </b:if>
    </span>
  </span>
</b:includable>
          <b:includable id='postCommentsLink'>
  <span class='byline post-comment-link container'>
    <b:include cond='data:post.commentSource != 1' name='commentsLink'/>
  </span>
</b:includable>
          <b:includable id='postContent' var='post'>
      <div class='post'>
        <div class='post-content'>
          <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
            <span class='post-tag'><data:post.labels.last.name/></span>
          </a>
          <div class='post-info'>
            <h2 class='post-title'>
              <a expr:href='data:post.url'><data:post.title/></a>
            </h2>
            <div class='post-meta'>
              <span class='post-author'><a expr:href='data:post.author.profileUrl' expr:title='data:post.author.name' target='_blank'><data:post.author.name/></a></span><span class='post-date published' expr:datetime='data:post.date.iso8601'><data:post.date/></span>
            </div>
             <p class='post-snippet'><b:eval expr='data:post.snippets.long snippet { length: 100 }'/></p>
            <b:include data='post' name='postJumpLink'/>
          </div>
        </div>
      </div>
    </b:includable>
          <b:includable id='postJumpLink' var='post'>
  <div class='jump-link flat-button'>
    <a expr:href='data:post.url fragment &quot;more&quot;' expr:title='data:post.title'>
      Read More
    </a>
  </div>
</b:includable>
          <b:includable id='postLabels'>
  <span class='byline post-labels'>
    <span class='byline-label'><data:byline.label/></span>
    <b:loop index='i' values='data:post.labels' var='label'>
      <a expr:href='data:label.url' rel='tag'>
        <data:label.name/>
      </a>
    </b:loop>
  </span>
</b:includable>
          <b:includable id='postLocation'>
  <span class='byline post-location'>
    <data:byline.label/>
    <a expr:href='data:post.location.mapsUrl' target='_blank'><data:post.location.name/></a>
  </span>
</b:includable>
          <b:includable id='postReactions'>
  <!-- Reaction feature no longer available. The includable is retained for backwards-compatibility. -->
</b:includable>
          <b:includable id='postShareButtons'>
  <div class='byline post-share-buttons goog-inline-block'>
    <b:with value='data:sharingId ?: ((data:widget.instanceId ?: &quot;sharing&quot;) + &quot;-&quot; + (data:regionName ?: &quot;byline&quot;) + &quot;-&quot; + data:post.id)' var='sharingId'>
      <!-- Note: 'sharingButtons' includable is from the default Sharing widget markup. -->
      <b:include data='{                                                sharingId: data:sharingId,                                                originalUrl: data:post.url,                                                platforms: data:this.sharing.platforms,                                                shareUrl: data:post.shareUrl,                                                shareTitle: data:post.title,                                              }' name='sharingButtons'/>
    </b:with>
  </div>
</b:includable>
          <b:includable id='postTimestamp'>
  <span class='byline post-timestamp'>
    <data:byline.label/>
    <b:if cond='data:post.url'>
      <meta expr:content='data:post.url.canonical'/>
      <a class='timestamp-link' expr:href='data:post.url' rel='bookmark' title='permanent link'>
        <time class='published' expr:datetime='data:post.date.iso8601' expr:title='data:post.date.iso8601'>
          <data:post.date/>
        </time>
      </a>
    </b:if>
  </span>
</b:includable>
          <b:includable id='sharingButton'>
  <span expr:aria-label='data:platform.shareMessage' expr:class='&quot;sharing-platform-button sharing-element-&quot; + data:platform.key' expr:data-href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:data-url='data:originalUrl' expr:title='data:platform.shareMessage' role='menuitem' tabindex='-1'>
    <b:include name='sharingPlatformIcon'/>
    <span class='platform-sharing-text'><data:platform.name/></span>
  </span>
</b:includable>
          <b:includable id='sharingButtonContent'>
  <div class='flat-icon-button ripple'>
    <b:include name='shareIcon'/>
  </div>
</b:includable>
          <b:includable id='sharingButtons'>
  <div class='sharing' expr:aria-owns='&quot;sharing-popup-&quot; + data:sharingId' expr:data-title='data:shareTitle'>
    <button class='sharing-button touch-icon-button' expr:aria-controls='&quot;sharing-popup-&quot; + data:sharingId' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-button-&quot; + data:sharingId' role='button'>
      <b:include name='sharingButtonContent'/>
    </button>
    <b:include name='sharingButtonsMenu'/>
  </div>
</b:includable>
          <b:includable id='sharingButtonsMenu'>
  <div class='share-buttons-container'>
    <ul aria-hidden='true' class='share-buttons hidden' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-popup-&quot; + data:sharingId' role='menu'>
      <b:loop values='(data:platforms ?: data:blog.sharing.platforms) filter (p =&gt; p.key not in {&quot;blogThis&quot;})' var='platform'>
        <li>
          <b:include name='sharingButton'/>
        </li>
      </b:loop>
      <li aria-hidden='true' class='hidden'>
        <b:include name='otherSharingButton'/>
      </li>
    </ul>
  </div>
</b:includable>
          <b:includable id='sharingPlatformIcon'>
  <b:include data='{ iconClass: (&quot;touch-icon sharing-&quot; + data:platform.key) }' expr:name='data:platform.key + &quot;Icon&quot;'/>
</b:includable>
          <b:includable id='snippetedPostByline'>
  <b:with value='(data:widgets first (w =&gt; w.type == &quot;Blog&quot;)).allBylineItems' var='blogBylines'>
    <div class='item-byline'>
      <b:with value='data:blogBylines first (i =&gt; i.name == &quot;author&quot;)' var='byline'>
        <b:include cond='data:byline and data:this.postDisplay.showAuthor' data='post' name='postAuthor'/>
      </b:with>
      <b:with value='data:blogBylines first (i =&gt; i.name == &quot;timestamp&quot;)' var='byline'>
        <b:include cond='data:byline and data:this.postDisplay.showDate' data='post' name='postTimestamp'/>
      </b:with>
    </div>
  </b:with>
</b:includable>
          <b:includable id='snippetedPostContent'>
  <div class='post-content'>
    <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
    <b:include cond='data:this.postDisplay.showDate or data:this.postDisplay.showAuthor' name='snippetedPostByline'/>
    <b:include cond='data:this.postDisplay.showSnippet' data='post' name='postSnippet'/>
    <b:include cond='data:this.postDisplay.showFeaturedImage and data:post.featuredImage' name='snippetedPostThumbnail'/>
  </div>
</b:includable>
          <b:includable id='snippetedPostThumbnail'>
  <div class='item-thumbnail'>
    <a expr:href='data:post.url'>
      <b:include data='{                         image: data:post.featuredImage,                         imageSizes: [72, 144],                         imageRatio: &quot;1:1&quot;,                         sourceSizes: &quot;72px&quot;                        }' name='responsiveImage'/>
    </a>
  </div>
</b:includable>
          <b:includable id='snippetedPostTitle'>
  <b:if cond='data:post.title != &quot;&quot;'>
    <h3 class='post-title'><a expr:href='data:post.url'><data:post.title/></a></h3>
  </b:if>
</b:includable>
          <b:includable id='snippetedPosts'>
  <div role='feed'>
    <!-- Don't render the post that we're currently already looking at. -->
    <b:loop values='data:posts filter (p =&gt; p.id != data:view.postId)' var='post'>
      <article class='post' role='article'>
        <b:include name='snippetedPostContent'/>
      </article>
    </b:loop>
  </div>
</b:includable>
        </b:widget>
      </b:section>
    </div>
    <div class='clearfix'/>
    <!-- Featured Wrapper -->
    
 <b:section class='home-ad' id='home-ad-top2' maxwidgets='1' name='Home Ads 2' showaddelement='yes'>
   <b:widget id='HTML22' locked='false' title='Ad Code' type='HTML' visible='false'>
     <b:widget-settings>
       <b:widget-setting name='content'><![CDATA[<a class="sora-ads-full" href="javascript:;">Responsive Advertisement</a>]]></b:widget-setting>
     </b:widget-settings>
     <b:includable id='main'>
  <b:include name='widget-title'/>
  <div class='widget-content'>
    <data:content/>
  </div>
</b:includable>
   </b:widget>
 </b:section>
    <div class='clearfix'/>
        </b:if>

        <b:section class='main' id='main' maxwidgets='1' name='Main Posts' showaddelement='yes'>
          <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='2' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='showDateHeader'>false</b:widget-setting>
              <b:widget-setting name='commentLabel'>Comments</b:widget-setting>
              <b:widget-setting name='style.textcolor'>#ffffff</b:widget-setting>
              <b:widget-setting name='showShareButtons'>true</b:widget-setting>
              <b:widget-setting name='authorLabel'>by</b:widget-setting>
              <b:widget-setting name='showCommentLink'>true</b:widget-setting>
              <b:widget-setting name='style.urlcolor'>#ffffff</b:widget-setting>
              <b:widget-setting name='showAuthor'>true</b:widget-setting>
              <b:widget-setting name='style.linkcolor'>#ffffff</b:widget-setting>
              <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
              <b:widget-setting name='style.bgcolor'>#ffffff</b:widget-setting>
              <b:widget-setting name='timestampLabel'/>
              <b:widget-setting name='reactionsLabel'/>
              <b:widget-setting name='showAuthorProfile'>true</b:widget-setting>
              <b:widget-setting name='style.layout'>1x1</b:widget-setting>
              <b:widget-setting name='showLabels'>true</b:widget-setting>
              <b:widget-setting name='showLocation'>false</b:widget-setting>
              <b:widget-setting name='postLabelsLabel'>Tags</b:widget-setting>
              <b:widget-setting name='showTimestamp'>true</b:widget-setting>
              <b:widget-setting name='postsPerAd'>1</b:widget-setting>
              <b:widget-setting name='showBacklinks'>false</b:widget-setting>
              <b:widget-setting name='style.bordercolor'>#ffffff</b:widget-setting>
              <b:widget-setting name='showInlineAds'>false</b:widget-setting>
              <b:widget-setting name='showReactions'>false</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main' var='this'>
              <b:include name='homePostsHeadline'/>
              <b:include name='searchMessage'/>
              <div class='blog-posts hfeed container'>
                <b:class cond='data:view.isMultipleItems' name='index-post-wrap'/>
                <b:class cond='data:view.isSingleItem' name='item-post-wrap'/>
                <b:tag class='grid-posts' cond='data:view.isMultipleItems' name='div'>
                  <b:loop index='i' values='data:posts' var='post'>
                    <b:include data='post' name='postCommentsAndAd'/>
                  </b:loop>
                </b:tag>
              </div>
              <b:include cond='data:view.isMultipleItems' name='indexBlogPager'/>
              <b:include name='feedLinks'/>
            </b:includable>
            <b:includable id='aboutPostAuthor'>
              <div class='about-author'>
                <div class='avatar-container'>
                  <b:if cond='data:post.author.authorPhoto.image'>
                    <img class='author-avatar' expr:alt='data:post.author.name' expr:src='data:post.author.authorPhoto.image resizeImage 100'/>                
                    <b:else/>
                    <img class='author-avatar' expr:alt='data:post.author.name' src='https://4.bp.blogspot.com/-uCjYgVFIh70/VuOLn-mL7PI/AAAAAAAADUs/Kcu9wJbv790hIo83rI_s7lLW3zkLY01EA/s100/avatar.png'/>
                  </b:if>
                </div>
                <h3 class='author-name'>
                  <span><data:messages.postedBy/></span><a expr:alt='data:post.author.name' expr:href='data:post.author.profileUrl' target='_blank'> <data:post.author.name/></a>
                </h3>
                <span class='author-description'><data:post.author.aboutMe/></span>
              </div>
            </b:includable>
            <b:includable id='addComments'>
              <a expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
                <b:message name='messages.postAComment'/>
              </a>
            </b:includable>
            <b:includable id='backLinks' var='post'>
              <b:comment>Disabled</b:comment>         
            </b:includable>
            <b:includable id='blogThisShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=270,width=475\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='bylineByName' var='byline'>
  <b:switch var='data:byline.name'>
  <b:case value='share'/>
    <b:include cond='data:post.shareUrl' name='postShareButtons'/>
  <b:case value='comments'/>
    <b:include cond='data:post.allowComments' name='postCommentsLink'/>
  <b:case value='location'/>
    <b:include cond='data:post.location' name='postLocation'/>
  <b:case value='timestamp'/>
    <b:include cond='not data:view.isPage' name='postTimestamp'/>
  <b:case value='author'/>
    <b:include name='postAuthor'/>
  <b:case value='labels'/>
    <b:include cond='data:post.labels' name='postLabels'/>
  <b:case value='icons'/>
    <b:include cond='data:post.emailPostUrl' name='emailPostIcon'/>
  <b:case value='reactions'/>
    <b:include cond='data:post.reactionsUrl' name='postReactions'/>
  </b:switch>
</b:includable>
            <b:includable id='bylineRegion' var='regionItems'>
  <b:loop values='data:regionItems' var='byline'>
    <b:include data='byline' name='bylineByName'/>
  </b:loop>
</b:includable>
            <b:includable id='commentAuthorAvatar'>
              <div class='avatar-image-container'>
                <img class='author-avatar' expr:src='data:comment.authorAvatarSrc' height='45' width='45'/>
              </div>
            </b:includable>
            <b:includable id='commentDeleteIcon' var='comment'>
              <span expr:class='&quot;item-control &quot; + data:comment.adminClass'>
                <b:if cond='data:showCmtPopup'>
                  <div class='goog-toggle-button'>
                    <div class='goog-inline-block comment-action-icon'/>
                  </div>
                  <b:else/>
                  <a class='comment-delete' expr:href='data:comment.deleteUrl' expr:title='data:messages.deleteComment'>
                    <img src='https://resources.blogblog.com/img/icon_delete13.gif'/>
                  </a>
                </b:if>
              </span>
            </b:includable>
            <b:includable id='commentForm' var='post'>
              <div class='comment-form'>
                <a name='comment-form'/>
                <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
                  <p><data:this.messages.blogComment/></p>
                </b:if>
                <b:include data='post' name='commentFormIframeSrc'/>
                <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
                <data:post.cmtfpIframe/>
                <script type='text/javascript'>
                  BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
                </script>
              </div>
            </b:includable>
            <b:includable id='commentFormIframeSrc' var='post'>
              <a expr:href='data:post.commentFormIframeSrc + &quot;&amp;skin=contempo&quot;' id='comment-editor-src'/>
            </b:includable>
            <b:includable id='commentItem' var='comment'>
              <div class='comment' expr:id='&quot;c&quot; + data:comment.id'>
                <b:include cond='data:blog.enabledCommentProfileImages' name='commentAuthorAvatar'/>

                <div class='comment-block'>
                  <div class='comment-author'>
                    <b:if cond='data:comment.authorUrl'>
                      <b:message name='messages.authorSaidWithLink'>
                        <b:param expr:value='data:comment.author' name='authorName'/>
                        <b:param expr:value='data:comment.authorUrl' name='authorUrl'/>
                      </b:message>
                      <b:else/>
                      <b:message name='messages.authorSaid'>
                        <b:param expr:value='data:comment.author' name='authorName'/>
                      </b:message>
                    </b:if>
                  </div>
                  <div expr:class='&quot;comment-body&quot; + (data:comment.isDeleted ? &quot; deleted&quot; : &quot;&quot;)'>
                    <data:comment.body/>
                  </div>
                  <div class='comment-footer'>
                    <span class='comment-timestamp'>
                      <a expr:href='data:comment.url' title='comment permalink'>
                        <data:comment.timestamp/>
                      </a>
                      <b:include data='comment' name='commentDeleteIcon'/>
                    </span>
                  </div>
                </div>
              </div>
            </b:includable>
            <b:includable id='commentList' var='comments'>
              <div id='comments-block'>
                <b:loop values='data:comments' var='comment'>
                  <b:include data='comment' name='commentItem'/>
                </b:loop>
              </div>
            </b:includable>
            <b:includable id='commentPicker' var='post'>
              <b:if cond='data:post.allowComments'>
                <div class='title-wrap comments-title'>
                  <h3><data:messages.postAComment/></h3>
                </div>
              </b:if>
              <b:if cond='data:post.commentSource == 1'>
                <b:include data='post' name='iframeComments'/>
                <b:elseif cond='data:post.showThreadedComments'/>
                <b:include data='post' name='threadedComments'/>
                <b:else/>
                <b:include data='post' name='comments'/>
              </b:if>
            </b:includable>
            <b:includable id='comments' var='post'>
              <section expr:class='&quot;comments&quot; + (data:post.embedCommentForm ? &quot; embed&quot; : &quot;&quot;)' expr:data-num-comments='data:post.numberOfComments' id='comments'>
                <a name='comments'/>
                <b:if cond='data:post.allowComments'>

                  <b:include name='commentsTitle'/>

                  <div expr:id='data:widget.instanceId + &quot;_comments-block-wrapper&quot;'>
                    <b:include cond='data:post.comments' data='post.comments' name='commentList'/>
                  </div>

                  <b:if cond='data:post.commentPagingRequired'>
                    <div class='paging-control-container'>
                      <b:if cond='data:post.hasOlderLinks'>
                        <a expr:class='data:post.oldLinkClass' expr:href='data:post.oldestLinkUrl'>
                          <data:messages.oldest/>
                        </a>
                        <a expr:class='data:post.oldLinkClass' expr:href='data:post.olderLinkUrl'>
                          <data:messages.older/>
                        </a>
                      </b:if>

                      <span class='comment-range-text'>
                        <data:post.commentRangeText/>
                      </span>

                      <b:if cond='data:post.hasNewerLinks'>
                        <a expr:class='data:post.newLinkClass' expr:href='data:post.newerLinkUrl'>
                          <data:messages.newer/>
                        </a>
                        <a expr:class='data:post.newLinkClass' expr:href='data:post.newestLinkUrl'>
                          <data:messages.newest/>
                        </a>
                      </b:if>
                    </div>
                  </b:if>

                  <div class='footer'>
                    <b:if cond='data:post.embedCommentForm'>
                      <b:if cond='data:post.allowNewComments'>
                        <b:include data='post' name='commentForm'/>
                        <b:else/>
                        <data:post.noNewCommentsText/>
                      </b:if>
                      <b:else/>
                      <b:if cond='data:post.allowComments'>
                        <b:include data='post' name='addComments'/>
                      </b:if>
                    </b:if>
                  </div>
                </b:if>
                <b:if cond='data:showCmtPopup'>
                  <div id='comment-popup'>
                    <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
                    </iframe>
                  </div>
                </b:if>
              </section>
            </b:includable>
            <b:includable id='commentsLink'>
  <a class='comment-link' expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
    <b:if cond='data:post.numberOfComments &gt; 0'>
      <b:message name='messages.numberOfComments'>
        <b:param expr:value='data:post.numberOfComments' name='numComments'/>
      </b:message>
    <b:else/>
      <data:messages.postAComment/>
    </b:if>
  </a>
</b:includable>
            <b:includable id='commentsLinkIframe'>
  <!-- G+ comments, no longer available. The includable is retained for backwards-compatibility. -->
</b:includable>
            <b:includable id='commentsTitle'>
              <!-- Post Commments Title -->
              <h3 class='title'><data:post.numberOfComments/> <data:messages.comments/></h3>
            </b:includable>
            <b:includable id='defaultAdUnit'>
  <ins class='adsbygoogle' data-ad-format='auto' expr:data-ad-client='data:adClientId ?: data:blog.adsenseClientId' expr:data-ad-host='data:blog.adsenseHostId' expr:data-analytics-uacct='data:blog.analyticsAccountNumber' expr:style='data:style ?: &quot;display: block;&quot;'/>
  <script>
   (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</b:includable>
            <b:includable id='emailPostIcon'>
  <span class='byline post-icons'>
    <!-- email post links -->
    <span class='item-action'>
      <a expr:href='data:post.emailPostUrl' expr:title='data:messages.emailPost'>
        <b:include data='{ iconClass: &quot;touch-icon sharing-icon&quot; }' name='emailIcon'/>
      </a>
    </span>
  </span>
</b:includable>
            <b:includable id='facebookShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=430,width=640\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='feedLinks'>
              <b:comment>Disabled</b:comment> 
            </b:includable>
            <b:includable id='feedLinksBody' var='links'>
              <b:comment>Disabled</b:comment> 
            </b:includable>
            <b:includable id='footerBylines' var='post'>
              <!-- Post Footer Extras -->
              <b:include data='post' name='postLabels'/>
              <b:include data='post' name='postReactions'/>
              <b:include data='post' name='postShareButtons'/>
            </b:includable>
            <b:includable id='googlePlusShare'>
  <div class='goog-inline-block google-plus-share-container'>
    <g:plusone annotation='inline' expr:href='data:originalUrl.canonical.http' size='medium' source='blogger:blog:plusone'/>
  </div>
</b:includable>
            <b:includable id='headerByline' var='post'>
              <!-- Post Header Meta -->
                <div class='post-meta'>
                  <b:include data='post' name='postAuthor'/>
                  <b:include data='post' name='postTimestamp'/> 
                </div>
            </b:includable>
            <b:includable id='homePageLink'>
              <b:comment>Disabled</b:comment> 
            </b:includable>
            <b:includable id='homePostsHeadline'>
              <b:if cond='data:view.isHomepage'>
                <div class='home-posts-headline title-wrap Label'>           
                  <h3 class='title'><data:blog.jumpLinkMessage/></h3>  
                  <a class='view-all' href='/search'><data:messages.showMore/></a>   
                </div>
                <div class='clearfix'/>
              </b:if>
            </b:includable>
            <b:includable id='iframeComments' var='post'>
              <b:if cond='data:post.allowIframeComments'>
                <script expr:src='data:post.iframeCommentSrc' type='text/javascript'/>
                <div class='cmt_iframe_holder' expr:data-href='data:post.url.canonical' expr:data-viewtype='data:post.viewType'/>
                <b:if cond='!data:post.embedCommentForm'>
                  <b:include data='post' name='commentsLink'/>
                </b:if>
              </b:if>
            </b:includable>
            <b:includable id='indexBlogPager'>
             <!-- Post Pagination Index -->
              <div class='blog-pager container' id='blog-pager'>
                <b:if cond='data:olderPageUrl'>
                  <a class='blog-pager-older-link load-more' expr:data-load='data:olderPageUrl' href='javascript:;' id='load-more-link'><b:include data='{ message: &quot;loadMorePosts&quot; }' name='translate'/></a>
                  <span class='loading'><span class='loader'/></span>
                  <span class='no-more load-more'><b:include data='{ message: &quot;noMorePosts&quot; }' name='translate'/></span>
                  <b:else/>
                  <span class='no-more load-more show'><b:include data='{ message: &quot;noMorePosts&quot; }' name='translate'/></span>
                </b:if>
              </div>
            </b:includable>
            <b:includable id='indexPost' var='post'>
              <!-- Index Post Content -->
              <b:include data='post' name='postFeaturedImage'/>
              <div class='post-info'>
                <b:include data='post' name='postHeader'/>
                <b:include data='post' name='postSummary'/>
              </div>
            </b:includable>
            <b:includable id='inlineAd' var='post'>
              <b:comment>Disabled</b:comment> 
            </b:includable>
            <b:includable id='itemPost' var='post'>
              <!-- Item Post Content -->
              <b:include data='post' name='postMeta'/>
              <b:include data='post' name='postHeader'/>
              <b:include data='post' name='postBody'/>
              <b:include cond='data:view.isPost' data='post' name='postFooter'/>
            </b:includable>
            <b:includable id='linkShare'>
  <b:with value='&quot;window.prompt(\&quot;Copy to clipboard: Ctrl+C, Enter\&quot;, \&quot;&quot; + data:originalUrl + &quot;\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='manageComments'>
  <a expr:href='data:post.manageCommentsUrl' expr:onclick='data:post.manageCommentsUrlOnclick'>
    <b:message name='messages.manageComments'/>
  </a>
</b:includable>
            <b:includable id='messagesJs'>
              <script type='text/javascript'>
                var messages = { 
                  showMore: &quot;<data:messages.showMore/>&quot;
                }
              </script>
            </b:includable>
            <b:includable id='nextPageLink'>
              <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:messages.olderPosts'>
                <data:messages.loadMorePosts/>
              </a>
            </b:includable>
            <b:includable id='otherSharingButton'>
  <span class='sharing-platform-button sharing-element-other' expr:aria-label='data:messages.shareToOtherApps.escaped' expr:data-url='data:originalUrl' expr:title='data:messages.shareToOtherApps.escaped' role='menuitem' tabindex='-1'>
    <b:with value='{key: &quot;sharingOther&quot;}' var='platform'>
      <b:include name='sharingPlatformIcon'/>
    </b:with>
    <span class='platform-sharing-text'><data:messages.shareOtherApps.escaped/></span>
  </span>
</b:includable>
            <b:includable id='platformShare'>
  <a expr:class='&quot;goog-inline-block sharing-&quot; + data:platform.key' expr:data-url='data:originalUrl' expr:href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:onclick='data:onclick ? data:onclick : &quot;&quot;' expr:title='data:platform.shareMessage' target='_blank'>
    <span class='share-button-link-text'>
      <data:platform.shareMessage/>
    </span>
  </a>
</b:includable>
            <b:includable id='post' var='post'>
              <!-- Post Index -->
              <b:if cond='data:view.isMultipleItems'>
                <b:include data='post' name='indexPost'/>
              </b:if>
              <!-- Post Item -->
              <b:if cond='data:view.isSingleItem'>
                <b:include data='post' name='itemPost'/>
              </b:if>
            </b:includable>
            <b:includable id='postAuthor' var='post'>
              <!-- Post Author -->
              <b:if cond='data:allBylineItems.author'>
                <span class='post-author'><a expr:href='data:post.author.profileUrl' expr:title='data:post.author.name' target='_blank'><data:post.author.name/></a></span>
              </b:if>
            </b:includable>
            <b:includable id='postBody' var='post'> 
                         <!-- Ads before post content. -->
  
              <div class='post-body post-content' id='post-body'>
                <data:post.body/>
              </div>
                 <!-- Ads after post content. -->
      </b:includable>
            <b:includable id='postBodySnippet' var='post'>
              <b:include data='post' name='postBody'/>
            </b:includable>
            <b:includable id='postBreadcrumbs' var='post'>
              <!-- Post Breadcrumbs -->
              <nav id='breadcrumb'><a expr:href='data:blog.homepageUrl'><data:messages.home/></a><b:if cond='data:post.labels'><em class='delimiter'/><a class='b-label' expr:href='data:post.labels.last.url'><data:post.labels.last.name/></a></b:if><em class='delimiter'/><span class='current'><data:post.title/></span></nav>
              <script type='application/ld+json'>
              {
                &quot;@context&quot;: &quot;http://schema.org&quot;,
                &quot;@type&quot;: &quot;BreadcrumbList&quot;,
                &quot;@id&quot;: &quot;#Breadcrumb&quot;,
                &quot;itemListElement&quot;: [{
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: 1,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<data:messages.home/>&quot;,
                    &quot;@id&quot;: &quot;<data:blog.homepageUrl.jsonEscaped/>&quot;
                  }
                },{
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: 2,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<b:if cond='data:post.labels'><data:post.labels.last.name/></b:if>&quot;,
                    &quot;@id&quot;: &quot;<data:post.labels.last.url.jsonEscaped/>&quot;
                  }
                },{
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: 3,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<data:post.title/>&quot;,
                    &quot;@id&quot;: &quot;<data:post.url.jsonEscaped/>&quot;
                  }
                }]
              }
            </script>
            </b:includable>
            <b:includable id='postCategory' var='post'>
              <!-- Post Label/Category -->
              <b:if cond='data:view.isMultipleItems and data:post.labels'>
                <span class='post-tag index-post-tag'>
                  <i>in</i><span><data:post.labels.last.name/></span>
                </span>
              </b:if>
            </b:includable>
            <b:includable id='postCommentsAndAd' var='post'>
              <!-- Post, Comments and Ads -->
              <!-- Post Content Index and Item -->
              <div class='blog-post hentry'>
                <b:class cond='data:view.isMultipleItems' name='index-post'/>
                <b:class cond='data:view.isSingleItem' name='item-post'/>
                <b:include data='post' name='post'/>
              </div>
              <!-- Comments -->
              <b:if cond='data:view.isSingleItem'>
                <div class='blog-post-comments'>
                  <b:include data='post' name='threadedCommentsDisqus'/>
                  <b:include data='post' name='commentPicker'/>
                </div>
              </b:if>
            </b:includable>
            <b:includable id='postCommentsLink'>
              <b:if cond='data:view.isMultipleItems'>
                <span class='byline post-comment-link container'>
                  <b:include cond='data:post.commentSource != 1' name='commentsLink'/>
                  <b:include cond='data:post.commentSource == 1' name='commentsLinkIframe'/>
                </span>
              </b:if>
            </b:includable>
            <b:includable id='postFeaturedImage' var='post'>
              <!-- Post Featured Image on Index -->            
              <div class='post-image-wrap'>
                <a class='post-image-link' expr:href='data:post.url'>
                  <b:if cond='data:post.featuredImage'> 
                    <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
                    <b:else/>
                    <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
                  </b:if>
                </a>
              </div>         
            </b:includable>
            <b:includable id='postFooter' var='post'>
              <!-- Post Footer Itens -->
              <div class='post-footer'>
                <!-- Post Labels, Reactions, Share, Navigation, About Author an Related Posts -->
                <b:include data='post' name='footerBylines'/>
                <b:include data='post' name='postNavigation'/>
                <b:include data='post' name='aboutPostAuthor'/>
                <b:include data='post' name='postRelated'/>
              </div>
            </b:includable>
            <b:includable id='postFooterAuthorProfile' var='post'>
              <b:comment>Disabled</b:comment>   
            </b:includable>
            <b:includable id='postHeader' var='post'>
              <b:include cond='data:view.isPost' data='post' name='postBreadcrumbs'/>                
              <b:include cond='!data:view.isPage' data='post' name='postCategory'/>
              <b:include data='post' name='postTitle'/>
              <b:include cond='!data:view.isPage' data='post' name='headerByline'/>
            </b:includable>
            <b:includable id='postJumpLink' var='post'>
             <b:comment>Replaced</b:comment>
            </b:includable>
            <b:includable id='postLabels' var='post'>
              <b:if cond='data:allBylineItems.labels'>
                <b:if cond='data:post.labels'>
                  <div class='post-labels'>
                    <span><data:allBylineItems.labels.label/></span>
                    <div class='label-head Label'>
                      <b:loop values='data:post.labels' var='label'>
                        <a class='label-link' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                      </b:loop>
                    </div>
                  </div>
                </b:if>
              </b:if>
            </b:includable>
            <b:includable id='postLocation'>
  <span class='byline post-location'>
    <data:byline.label/>
    <a expr:href='data:post.location.mapsUrl' target='_blank'><data:post.location.name/></a>
  </span>
</b:includable>
            <b:includable id='postMeta' var='post'>
              <b:include data='post' name='postMetadataJSON'/>
            </b:includable>
            <b:includable id='postMetadataJSONImage'>
  &quot;image&quot;: {
    &quot;@type&quot;: &quot;ImageObject&quot;,
    <b:if cond='data:post.featuredImage.isResizable'>
    &quot;url&quot;: &quot;<b:eval expr='resizeImage(data:post.featuredImage, 1200, &quot;1200:630&quot;)'/>&quot;,
    &quot;height&quot;: 630,
    &quot;width&quot;: 1200
    <b:else/>
    &quot;url&quot;: &quot;https://lh3.googleusercontent.com/ULB6iBuCeTVvSjjjU1A-O8e9ZpVba6uvyhtiWRti_rBAs9yMYOFBujxriJRZ-A=w1200&quot;,
    &quot;height&quot;: 348,
    &quot;width&quot;: 1200
    </b:if>
  },
</b:includable>
            <b:includable id='postMetadataJSONPublisher'>
 &quot;publisher&quot;: {
    &quot;@type&quot;: &quot;Organization&quot;,
    &quot;name&quot;: &quot;Blogger&quot;,
    &quot;logo&quot;: {
      &quot;@type&quot;: &quot;ImageObject&quot;,
      &quot;url&quot;: &quot;https://lh3.googleusercontent.com/ULB6iBuCeTVvSjjjU1A-O8e9ZpVba6uvyhtiWRti_rBAs9yMYOFBujxriJRZ-A=h60&quot;,
      &quot;width&quot;: 206,
      &quot;height&quot;: 60
    }
  },
</b:includable>
            <b:includable id='postNavigation' var='post'>
              <!-- Post Navigation Item -->
              <ul class='post-nav'>
                <li class='post-next'> 
                  <b:if cond='data:newerPageUrl'> 
                    <a class='next-post-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' rel='next'>
                      <div class='post-nav-inner'><span><data:messages.newer/></span><p/></div>
                    </a> 
                    <b:else/> 
                    <a rel='next'><div class='post-nav-inner post-nav-active'><span><data:messages.newer/></span><p><data:post.title/></p></div></a> 
                  </b:if> 
                </li>
                <li class='post-prev'> 
                  <b:if cond='data:olderPageUrl'> 
                    <a class='prev-post-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' rel='previous'>
                      <div class='post-nav-inner'><span><data:messages.older/></span><p/></div>
                    </a> 
                    <b:else/>
                    <a rel='previous'><div class='post-nav-inner post-nav-active'><span><data:messages.older/></span><p><data:post.title/></p></div></a> 
                  </b:if> 
                </li>
              </ul>
            </b:includable>
            <b:includable id='postPagination'>
  <div class='blog-pager container' id='blog-pager'>
    <b:include cond='data:newerPageUrl' name='previousPageLink'/>
    <b:include cond='data:olderPageUrl' name='nextPageLink'/>
    <b:include cond='data:view.url != data:blog.homepageUrl' name='homePageLink'/>
  </div>
</b:includable>
            <b:includable id='postReactions' var='post'>
              <!-- Post Reactions -->
              <b:if cond='data:allBylineItems.reactions'>
                <div class='post-reactions'>
                  <span><data:allBylineItems.reactions.label/></span>
                  <div class='reactions-inner'>
                    <iframe allowtransparency='true' class='reactions-iframe' expr:src='data:posts[0].reactionsUrl' frameborder='0' name='reactions' scrolling='no'/>
                  </div>                  
                </div>
              </b:if>            
            </b:includable>
            <b:includable id='postRelated' var='post'>
              <!-- Related Posts -->
                <div id='related-wrap'>
                  <div class='title-wrap'>
                    <h3><data:messages.youMayLikeThesePosts/></h3>
                  </div>
                  <div class='related-ready'>
                    <b:if cond='data:post.labels'>
                      <div class='related-tag' expr:data-label='data:post.labels.first.name'/>
                      <b:else/>
                      <div class='related-tag' data-label='random'/>
                    </b:if>
                  </div> 
                </div>  
            </b:includable>
            <b:includable id='postShareButtons' var='post'>
              <!-- Post ShareButtons -->
              <b:if cond='data:allBylineItems.share'>
                <div class='post-share'>
                  <ul class='share-links social social-color'> 
                    <b:class cond='data:blog.isMobileRequest' name='is-mobile'/>
                    <li class='facebook'><a class='facebook' expr:href='&quot;https://www.facebook.com/sharer.php?u=&quot; + data:post.url' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=550, height=650, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'><span>Facebook</span></a></li>
                    <li class='twitter'><a class='twitter' expr:href='&quot;https://twitter.com/share?url=&quot; + data:post.url + &quot;&amp;text=&quot; + data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=550, height=450, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'><span>Twitter</span></a></li>
                  
                    <li class='pinterest'><a class='pinterest' expr:href='&quot;https://www.pinterest.com/pin/create/button/?url=&quot; + data:post.url + &quot;&amp;media=&quot; + data:post.featuredImage + &quot;&amp;description=&quot; + data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=735, height=750, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'/></li> 
                    <li class='linkedin'><a class='linkedin' expr:href='&quot;https://www.linkedin.com/shareArticle?url=&quot; + data:post.url' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=550, height=650, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'/></li>
                    <li class='whatsapp whatsapp-desktop'><a class='whatsapp' expr:href='&quot;https://web.whatsapp.com/send?text=&quot; + data:post.title + &quot; | &quot; + data:post.url' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=900, height=550, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'/></li>
                    <li class='whatsapp whatsapp-mobile'><a class='whatsapp' expr:href='&quot;https://api.whatsapp.com/send?text=&quot; + data:post.title + &quot; | &quot; + data:post.url' rel='nofollow' target='_blank'/></li>
                    <li class='email'><a class='email' expr:href='&quot;mailto:?subject=&quot; + data:post.title + &quot;&amp;body=&quot; + data:post.url' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=500, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow'/></li>
                  </ul>
                </div>
              </b:if>
            </b:includable>
            <b:includable id='postShortMeta'>
              <b:comment>Disabled</b:comment> 
            </b:includable>
            <b:includable id='postSummary' var='post'>
              <!-- Post Summary -->
              <p class='post-snippet'><b:eval expr='data:post.snippets.short snippet { length: 80 }'/></p>
            </b:includable>
            <b:includable id='postTimestamp' var='post'>
              <!-- Post Timestamp -->
              <b:if cond='data:allBylineItems.timestamp'>
                <span class='post-date published' expr:datetime='data:post.date.iso8601'><data:post.date/></span>
              </b:if>
            </b:includable>
            <b:includable id='postTitle' var='post'>
              <!-- Post Title Index and Item -->
              <b:if cond='data:view.isMultipleItems'>
                <h2 class='post-title'>
                  <a expr:href='data:post.url'><data:post.title/></a>
                </h2>
              </b:if>
              <b:if cond='data:view.isSingleItem'>
                <h1 class='post-title'>
                  <data:post.title/>
                </h1>
              </b:if>
            </b:includable>
            <b:includable id='previousPageLink'>
              <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:messages.newerPosts'>
                <data:messages.newerPosts/>
              </a>
            </b:includable>
            <b:includable id='searchMessage'>
              <!-- Search Message -->
              <b:if cond='data:view.search.query'>
                <div class='queryMessage'>
                  <b:if cond='data:posts.empty'>
                    <span class='query-info query-error'/><data:view.search.resultsMessageHtml/><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                    <b:else/>
                    <span class='query-info query-success'><data:view.search.resultsMessageHtml/></span><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                  </b:if>
                </div>
              </b:if>
              <b:if cond='data:view.search.label'>
                <div class='queryMessage'>
                  <b:if cond='data:posts.empty'>
                    <span class='query-info query-error'><data:view.search.resultsMessageHtml/></span><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                    <b:else/>
                    <span class='query-info query-success'><data:view.search.resultsMessageHtml/></span><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                  </b:if>
                </div>
              </b:if>
              <b:if cond='data:view.isArchive'>
                <div class='queryMessage'>
                  <b:if cond='data:posts.empty'>
                    <span class='query-info query-error'><data:view.archive.rangeMessage/></span><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                    <b:else/>
                    <span class='query-info query-success'><data:view.archive.rangeMessage/></span><a class='show-more' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                  </b:if>
                </div>
              </b:if>
              <b:if cond='data:view.isError'>
                <div class='errorWrap'>
                  <h3>404</h3>
                  <h4><data:messages.theresNothingHere/></h4>
                  <p><data:navMessage/></p>
                  <a class='homepage' expr:href='data:blog.homepageUrl'><i class='fa fa-home'/> <data:messages.home/></a>
                </div>
              </b:if>
              <b:if cond='data:view.isMultipleItems and data:posts.empty'><div class='queryEmpty'><data:messages.noResultsFound/></div></b:if>
            </b:includable>
            <b:includable id='sharingButton'>
  <span expr:aria-label='data:platform.shareMessage' expr:class='&quot;sharing-platform-button sharing-element-&quot; + data:platform.key' expr:data-href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:data-url='data:originalUrl' expr:title='data:platform.shareMessage' role='menuitem' tabindex='-1'>
    <b:include name='sharingPlatformIcon'/>
    <span class='platform-sharing-text'><data:platform.name/></span>
  </span>
</b:includable>
            <b:includable id='sharingButtonContent'>
  <div class='flat-icon-button ripple'>
    <b:include name='shareIcon'/>
  </div>
</b:includable>
            <b:includable id='sharingButtons'>
  <div class='sharing' expr:aria-owns='&quot;sharing-popup-&quot; + data:sharingId' expr:data-title='data:shareTitle'>
    <button class='sharing-button touch-icon-button' expr:aria-controls='&quot;sharing-popup-&quot; + data:sharingId' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-button-&quot; + data:sharingId' role='button'>
      <b:include name='sharingButtonContent'/>
    </button>
    <b:include name='sharingButtonsMenu'/>
  </div>
</b:includable>
            <b:includable id='sharingButtonsMenu'>
  <div class='share-buttons-container'>
    <ul aria-hidden='true' class='share-buttons hidden' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-popup-&quot; + data:sharingId' role='menu'>
      <b:loop values='(data:platforms ?: data:blog.sharing.platforms) filter (p =&gt; p.key not in {&quot;blogThis&quot;})' var='platform'>
        <li>
          <b:include name='sharingButton'/>
        </li>
      </b:loop>
      <li aria-hidden='true' class='hidden'>
        <b:include name='otherSharingButton'/>
      </li>
    </ul>
  </div>
</b:includable>
            <b:includable id='sharingPlatformIcon'>
  <b:include data='{ iconClass: (&quot;touch-icon sharing-&quot; + data:platform.key) }' expr:name='data:platform.key + &quot;Icon&quot;'/>
</b:includable>
            <b:includable id='threadedCommentForm' var='post'>
              <div class='comment-form'>
                <a name='comment-form'/>
                <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
                  <p><data:this.messages.blogComment/></p>
                </b:if>
                <b:include data='post' name='commentFormIframeSrc'/>
                <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
                <data:post.cmtfpIframe/>
                <script type='text/javascript'>
                  BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
                </script>
              </div>
            </b:includable>
            <b:includable id='threadedCommentJs' var='post'>
              <script async='async' expr:src='data:post.commentSrc' type='text/javascript'/>
              <b:template-script inline='true' name='threaded_comments'/>
              <script type='text/javascript'>
                blogger.widgets.blog.initThreadedComments(
                  <data:post.commentJso/>,
                  <data:post.commentMsgs/>,
                  <data:post.commentConfig/>);
              </script>
            </b:includable>
            <b:includable id='threadedComments' var='post'>
              <section class='comments threaded' expr:data-embed='data:post.embedCommentForm' expr:data-num-comments='data:post.numberOfComments' id='comments'>
                <a name='comments'/>

                <b:include name='commentsTitle'/>

                <div class='comments-content'>
                  <b:if cond='data:post.embedCommentForm'>
                    <b:include data='post' name='threadedCommentJs'/>
                  </b:if>
                  <div id='comment-holder'>
                    <data:post.commentHtml/>
                  </div>
                </div>

                <p class='comment-footer'>
                  <b:if cond='data:post.allowNewComments'>
                    <b:include data='post' name='threadedCommentForm'/>
                    <b:else/>
                    <data:post.noNewCommentsText/>
                  </b:if>
                </p>

                <b:if cond='data:showCmtPopup'>
                  <div id='comment-popup'>
                    <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
                    </iframe>
                  </div>
                </b:if>
              </section>
            </b:includable>
            <b:includable id='threadedCommentsDisqus' var='post'>
              <script type='text/javascript'>
                var disqus_blogger_current_url = &quot;<data:blog.canonicalUrl/>&quot;;
                if (!disqus_blogger_current_url.length) {
                  disqus_blogger_current_url = &quot;<data:blog.url/>&quot;;
                }
                var disqus_blogger_homepage_url = &quot;<data:blog.homepageUrl/>&quot;;
                var disqus_blogger_canonical_homepage_url = &quot;<data:blog.canonicalHomepageUrl/>&quot;;
              </script>
            </b:includable>
          </b:widget>
        </b:section> 
     
      </div>

      <!-- Sidebar Wrapper -->
      <div id='sidebar-wrapper'>
        <b:section class='sidebar common-widget' id='sidebar1' name='Sidebar Right (A)' showaddelement='yes'/>
        <b:section class='sidebar' id='social-widget' maxwidgets='1' name='Social Widget' showaddelement='yes'>
          <b:widget id='LinkList75' locked='true' title='Social Plugin' type='LinkList' version='2' visible='false'>
            <b:widget-settings>
              <b:widget-setting name='link-7'>#</b:widget-setting>
              <b:widget-setting name='link-5'>https://www.youtube.com/phidevs</b:widget-setting>
              <b:widget-setting name='link-6'>#</b:widget-setting>
              <b:widget-setting name='link-3'>#</b:widget-setting>
              <b:widget-setting name='link-4'>https://www.instagram.com/phidevs/</b:widget-setting>
              <b:widget-setting name='text-1'>twitter</b:widget-setting>
              <b:widget-setting name='text-0'>facebook</b:widget-setting>
              <b:widget-setting name='text-3'>pinterest</b:widget-setting>
              <b:widget-setting name='text-2'>reddit</b:widget-setting>
              <b:widget-setting name='text-5'>youtube</b:widget-setting>
              <b:widget-setting name='text-4'>instagram</b:widget-setting>
              <b:widget-setting name='text-7'>whatsapp</b:widget-setting>
              <b:widget-setting name='text-6'>linkedin</b:widget-setting>
              <b:widget-setting name='sorting'>NONE</b:widget-setting>
              <b:widget-setting name='link-1'>https://twitter.com/phidevs</b:widget-setting>
              <b:widget-setting name='link-2'>#</b:widget-setting>
              <b:widget-setting name='link-0'>https://www.facebook.com/phidevs/</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
            <b:includable id='content'>
              <div class='widget-content'>
                <ul class='social-counter social social-color'>
                  <b:loop values='data:links' var='link'>
                    <li expr:class='data:link.name'><a expr:href='data:link.target' expr:title='data:link.name' target='_blank'/></li>
                  </b:loop>
                </ul>
              </div>
            </b:includable>
          </b:widget>
        </b:section>
        <b:section class='sidebar common-widget' id='sidebar2' name='Sidebar Right (B)' showaddelement='yes'>
          <b:widget id='PopularPosts1' locked='false' title='Most Popular' type='PopularPosts' version='2' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='numItemsToShow'>3</b:widget-setting>
              <b:widget-setting name='showThumbnails'>true</b:widget-setting>
              <b:widget-setting name='showSnippets'>true</b:widget-setting>
              <b:widget-setting name='timeRange'>LAST_WEEK</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
          <b:tag class='main-slider' cond='data:widget.sectionId == &quot;slider-section&quot;' name='ul'>
        <b:loop index='i' values='data:posts' var='post'>
          <b:include data='post' name='postContent'/>
        </b:loop>
            </b:tag>
      </div>
    </b:includable>
            <b:includable id='blogThisShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=270,width=475\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='bylineByName' var='byline'>
  <b:switch var='data:byline.name'>
  <b:case value='share'/>
    <b:include cond='data:post.shareUrl' name='postShareButtons'/>
  <b:case value='comments'/>
    <b:include cond='data:post.allowComments' name='postCommentsLink'/>
  <b:case value='location'/>
    <b:include cond='data:post.location' name='postLocation'/>
  <b:case value='timestamp'/>
    <b:include cond='not data:view.isPage' name='postTimestamp'/>
  <b:case value='author'/>
    <b:include name='postAuthor'/>
  <b:case value='labels'/>
    <b:include cond='data:post.labels' name='postLabels'/>
  <b:case value='icons'/>
    <b:include cond='data:post.emailPostUrl' name='emailPostIcon'/>
  </b:switch>
</b:includable>
            <b:includable id='bylineRegion' var='regionItems'>
  <b:loop values='data:regionItems' var='byline'>
    <b:include data='byline' name='bylineByName'/>
  </b:loop>
</b:includable>
            <b:includable id='commentsLink'>
  <a class='comment-link' expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
    <b:if cond='data:post.numberOfComments &gt; 0'>
      <b:message name='messages.numberOfComments'>
        <b:param expr:value='data:post.numberOfComments' name='numComments'/>
      </b:message>
    <b:else/>
      <data:messages.postAComment/>
    </b:if>
  </a>
</b:includable>
            <b:includable id='commentsLinkIframe'>
  <!-- G+ comments, no longer available. The includable is retained for backwards-compatibility. -->
</b:includable>
            <b:includable id='default' var='post'>
       <div class='post default-popularpost'>  
              <b:class expr:name='&quot;item-&quot;+data:i'/>
        <div class='post-content'>
          <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
          </a>
          <div class='post-info'>
            <h2 class='post-title'>
              <a expr:href='data:post.url'><data:post.title/></a>
            </h2>
            <div class='post-meta'>
              <span class='post-date published' expr:datetime='data:post.date.iso8601'><data:post.date/></span>
            </div>
          </div>
        </div>
      </div>
    </b:includable>
            <b:includable id='emailPostIcon'>
  <span class='byline post-icons'>
    <!-- email post links -->
    <span class='item-action'>
      <a expr:href='data:post.emailPostUrl' expr:title='data:messages.emailPost'>
        <b:include data='{ iconClass: &quot;touch-icon sharing-icon&quot; }' name='emailIcon'/>
      </a>
    </span>
  </span>
</b:includable>
            <b:includable id='facebookShare'>
  <b:with value='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=430,width=640\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='footerBylines'>
  <b:if cond='data:widgets.Blog.first.footerBylines'>
    <b:loop index='i' values='data:widgets.Blog.first.footerBylines' var='region'>
      <b:if cond='not data:region.items.empty'>
        <div expr:class='&quot;post-footer-line post-footer-line-&quot; + (data:i + 1)'>
          <b:with value='&quot;footer-&quot; + (data:i + 1)' var='regionName'>
            <b:include data='region.items' name='bylineRegion'/>
          </b:with>
        </div>
      </b:if>
    </b:loop>
  </b:if>
</b:includable>
            <b:includable id='googlePlusShare'>
  <div class='goog-inline-block google-plus-share-container'>
    <g:plusone annotation='inline' expr:href='data:originalUrl.canonical.http' size='medium' source='blogger:blog:plusone'/>
  </div>
</b:includable>
            <b:includable id='headerByline'>
  <b:if cond='data:widgets.Blog.first.headerByline'>
    <div class='post-header'>
      <div class='post-header-line-1'>
        <b:with value='&quot;header-1&quot;' var='regionName'>
          <b:include data='data:widgets.Blog.first.headerByline.items' name='bylineRegion'/>
        </b:with>
      </div>
    </div>
  </b:if>
</b:includable>
            <b:includable id='linkShare'>
  <b:with value='&quot;window.prompt(\&quot;Copy to clipboard: Ctrl+C, Enter\&quot;, \&quot;&quot; + data:originalUrl + &quot;\&quot;); return false;&quot;' var='onclick'>
    <b:include name='platformShare'/>
  </b:with>
</b:includable>
            <b:includable id='otherSharingButton'>
  <span class='sharing-platform-button sharing-element-other' expr:aria-label='data:messages.shareToOtherApps.escaped' expr:data-url='data:originalUrl' expr:title='data:messages.shareToOtherApps.escaped' role='menuitem' tabindex='-1'>
    <b:with value='{key: &quot;sharingOther&quot;}' var='platform'>
      <b:include name='sharingPlatformIcon'/>
    </b:with>
    <span class='platform-sharing-text'><data:messages.shareOtherApps.escaped/></span>
  </span>
</b:includable>
            <b:includable id='platformShare'>
  <a expr:class='&quot;goog-inline-block sharing-&quot; + data:platform.key' expr:data-url='data:originalUrl' expr:href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:onclick='data:onclick ? data:onclick : &quot;&quot;' expr:title='data:platform.shareMessage' target='_blank'>
    <span class='share-button-link-text'>
      <data:platform.shareMessage/>
    </span>
  </a>
</b:includable>
            <b:includable id='postAuthor'>
  <span class='byline post-author vcard'>
    <span class='post-author-label'>
      <data:byline.label/>
    </span>
    <span class='fn'>
      <b:if cond='data:post.author.profileUrl'>
        <meta expr:content='data:post.author.profileUrl'/>
        <a class='g-profile' expr:href='data:post.author.profileUrl' rel='author' title='author profile'>
          <span><data:post.author.name/></span>
        </a>
      <b:else/>
        <span><data:post.author.name/></span>
      </b:if>
    </span>
  </span>
</b:includable>
            <b:includable id='postCommentsLink'>
  <span class='byline post-comment-link container'>
    <b:include cond='data:post.commentSource != 1' name='commentsLink'/>
  </span>
</b:includable>
            <b:includable id='postContent' var='post'>
       <b:if cond='data:widget.sectionId == &quot;slider-section&quot;'>
        <b:include data='post' name='slider-section'/>
        <b:else/>
        <b:include data='post' name='default'/>
      </b:if>
    </b:includable>
            <b:includable id='postJumpLink' var='post'>
  <div class='jump-link flat-button'>
    <a expr:href='data:post.url fragment &quot;more&quot;' expr:title='data:post.title'>
      <b:eval expr='data:blog.jumpLinkMessage'/>
    </a>
  </div>
</b:includable>
            <b:includable id='postLabels'>
  <span class='byline post-labels'>
    <span class='byline-label'><data:byline.label/></span>
    <b:loop index='i' values='data:post.labels' var='label'>
      <a expr:href='data:label.url' rel='tag'>
        <data:label.name/>
      </a>
    </b:loop>
  </span>
</b:includable>
            <b:includable id='postLocation'>
  <span class='byline post-location'>
    <data:byline.label/>
    <a expr:href='data:post.location.mapsUrl' target='_blank'><data:post.location.name/></a>
  </span>
</b:includable>
            <b:includable id='postReactions'>
  <!-- Reaction feature no longer available. The includable is retained for backwards-compatibility. -->
</b:includable>
            <b:includable id='postShareButtons'>
  <div class='byline post-share-buttons goog-inline-block'>
    <b:with value='data:sharingId ?: ((data:widget.instanceId ?: &quot;sharing&quot;) + &quot;-&quot; + (data:regionName ?: &quot;byline&quot;) + &quot;-&quot; + data:post.id)' var='sharingId'>
      <!-- Note: 'sharingButtons' includable is from the default Sharing widget markup. -->
      <b:include data='{                                                sharingId: data:sharingId,                                                originalUrl: data:post.url,                                                platforms: data:this.sharing.platforms,                                                shareUrl: data:post.shareUrl,                                                shareTitle: data:post.title,                                              }' name='sharingButtons'/>
    </b:with>
  </div>
</b:includable>
            <b:includable id='postTimestamp'>
  <span class='byline post-timestamp'>
    <data:byline.label/>
    <b:if cond='data:post.url'>
      <meta expr:content='data:post.url.canonical'/>
      <a class='timestamp-link' expr:href='data:post.url' rel='bookmark' title='permanent link'>
        <time class='published' expr:datetime='data:post.date.iso8601' expr:title='data:post.date.iso8601'>
          <data:post.date/>
        </time>
      </a>
    </b:if>
  </span>
</b:includable>
            <b:includable id='sharingButton'>
  <span expr:aria-label='data:platform.shareMessage' expr:class='&quot;sharing-platform-button sharing-element-&quot; + data:platform.key' expr:data-href='data:shareUrl + &quot;&amp;target=&quot; + data:platform.target' expr:data-url='data:originalUrl' expr:title='data:platform.shareMessage' role='menuitem' tabindex='-1'>
    <b:include name='sharingPlatformIcon'/>
    <span class='platform-sharing-text'><data:platform.name/></span>
  </span>
</b:includable>
            <b:includable id='sharingButtonContent'>
  <div class='flat-icon-button ripple'>
    <b:include name='shareIcon'/>
  </div>
</b:includable>
            <b:includable id='sharingButtons'>
  <div class='sharing' expr:aria-owns='&quot;sharing-popup-&quot; + data:sharingId' expr:data-title='data:shareTitle'>
    <button class='sharing-button touch-icon-button' expr:aria-controls='&quot;sharing-popup-&quot; + data:sharingId' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-button-&quot; + data:sharingId' role='button'>
      <b:include name='sharingButtonContent'/>
    </button>
    <b:include name='sharingButtonsMenu'/>
  </div>
</b:includable>
            <b:includable id='sharingButtonsMenu'>
  <div class='share-buttons-container'>
    <ul aria-hidden='true' class='share-buttons hidden' expr:aria-label='data:messages.share.escaped' expr:id='&quot;sharing-popup-&quot; + data:sharingId' role='menu'>
      <b:loop values='(data:platforms ?: data:blog.sharing.platforms) filter (p =&gt; p.key not in {&quot;blogThis&quot;})' var='platform'>
        <li>
          <b:include name='sharingButton'/>
        </li>
      </b:loop>
      <li aria-hidden='true' class='hidden'>
        <b:include name='otherSharingButton'/>
      </li>
    </ul>
  </div>
</b:includable>
            <b:includable id='sharingPlatformIcon'>
  <b:include data='{ iconClass: (&quot;touch-icon sharing-&quot; + data:platform.key) }' expr:name='data:platform.key + &quot;Icon&quot;'/>
</b:includable>
            <b:includable id='slider-section' var='post'>
         <b:if cond='data:i lt 10'>
           <li class='slider-item'>
              <b:class expr:name='&quot;item-&quot;+data:i'/>
               <a class='post-image-link' expr:href='data:post.url'>
            <b:if cond='data:post.featuredImage'>
              <img class='post-thumb' expr:alt='data:post.title' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 72, &quot;1:1&quot;) : resizeImage(data:post.featuredImage, 72, &quot;1:1&quot;)'/>
              <b:else/>
              <img class='post-thumb' expr:alt='data:post.title' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
            </b:if>
          </a>
              <div class='post-info-wrap'><div class='post-info'>
              <b:if cond='data:post.labels'><span class='post-tag'><data:post.labels.first.name/></span></b:if>
               <h2 class='post-title'>
               <a expr:href='data:post.url'><data:post.title/></a>
               </h2>
               </div></div>
           </li>
           </b:if>
       </b:includable>
            <b:includable id='snippetedPostByline'>
  <b:with value='(data:widgets first (w =&gt; w.type == &quot;Blog&quot;)).allBylineItems' var='blogBylines'>
    <div class='item-byline'>
      <b:with value='data:blogBylines first (i =&gt; i.name == &quot;author&quot;)' var='byline'>
        <b:include cond='data:byline and data:this.postDisplay.showAuthor' data='post' name='postAuthor'/>
      </b:with>
      <b:with value='data:blogBylines first (i =&gt; i.name == &quot;timestamp&quot;)' var='byline'>
        <b:include cond='data:byline and data:this.postDisplay.showDate' data='post' name='postTimestamp'/>
      </b:with>
    </div>
  </b:with>
</b:includable>
            <b:includable id='snippetedPostContent'>
  <div class='post-content'>
    <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
    <b:include cond='data:this.postDisplay.showDate or data:this.postDisplay.showAuthor' name='snippetedPostByline'/>
    <b:include cond='data:this.postDisplay.showSnippet' data='post' name='postSnippet'/>
    <b:include cond='data:this.postDisplay.showFeaturedImage and data:post.featuredImage' name='snippetedPostThumbnail'/>
  </div>
</b:includable>
            <b:includable id='snippetedPostThumbnail'>
  <div class='item-thumbnail'>
    <a expr:href='data:post.url'>
      <b:include data='{                         image: data:post.featuredImage,                         imageSizes: [72, 144],                         imageRatio: &quot;1:1&quot;,                         sourceSizes: &quot;72px&quot;                        }' name='responsiveImage'/>
    </a>
  </div>
</b:includable>
            <b:includable id='snippetedPostTitle'>
  <b:if cond='data:post.title != &quot;&quot;'>
    <h3 class='post-title'><a expr:href='data:post.url'><data:post.title/></a></h3>
  </b:if>
</b:includable>
            <b:includable id='snippetedPosts'>
  <div role='feed'>
    <!-- Don't render the post that we're currently already looking at. -->
    <b:loop values='data:posts filter (p =&gt; p.id != data:view.postId)' var='post'>
      <article class='post' role='article'>
        <b:include name='snippetedPostContent'/>
      </article>
    </b:loop>
  </div>
</b:includable>
          </b:widget>
          <b:widget id='HTML6' locked='false' title='Facebook' type='HTML' visible='false'>
            <b:widget-settings>
              <b:widget-setting name='content'><![CDATA[<center><div class="fb-page" data-href="https://www.facebook.com/phidevs" data-width="360" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"></div></center>]]></b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
  <b:include name='widget-title'/>
  <div class='widget-content'>
    <data:content/>
  </div>
</b:includable>
          </b:widget>
          <b:widget id='Label4' locked='false' title='Tags' type='Label' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
              <b:widget-setting name='display'>CLOUD</b:widget-setting>
              <b:widget-setting name='selectedLabelsList'>Beauty,Business,Fashion,Learn,Music,Nature,People,Photography,Sports,Technology</b:widget-setting>
              <b:widget-setting name='showType'>USER_SELECTED</b:widget-setting>
              <b:widget-setting name='showFreqNumbers'>false</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
            <b:includable id='cloud'>
  <b:loop values='data:labels' var='label'>
    <span class='label-size'>
      <b:class expr:name='&quot;label-size-&quot; + data:label.cssSize'/>
      <a class='label-name' expr:href='data:label.url'>
        <data:label.name/>
        <b:if cond='data:this.showFreqNumbers'>
          <span class='label-count'><data:label.count/></span>
        </b:if>
      </a>
    </span>
  </b:loop>
</b:includable>
            <b:includable id='content'>
      <div class='widget-content'>
        <b:class expr:name='data:this.display + &quot;-label&quot;'/>
        <b:include cond='data:this.display == &quot;list&quot;' name='list'/>
        <b:include cond='data:this.display == &quot;cloud&quot;' name='list'/>
      </div>
    </b:includable>
            <b:includable id='list'>
      <ul>
        <b:loop values='data:labels' var='label'>
          <li>
            <a class='label-name' expr:href='data:label.url'>
              <data:label.name/>
              <b:if cond='data:this.showFreqNumbers'>
                <span class='label-count'><data:label.count/></span>
              </b:if>
            </a>
          </li>
        </b:loop>
      </ul>
    </b:includable>
          </b:widget>
        </b:section>
        </div>
      </div>
  </div>

 <div class='clearfix'/>
  </div>
  <b:section class='row home-ad' id='footer-ads' maxwidgets='1' name='Footer Ads' showaddelement='yes'>
    <b:widget id='HTML39' locked='false' title='Advertisement' type='HTML' version='2' visible='false'>
      <b:widget-settings>
        <b:widget-setting name='content'><![CDATA[<a class="sora-ads-full" href="javascript:;">Responsive Advertisement</a>]]></b:widget-setting>
      </b:widget-settings>
      <b:includable id='main'>
                <b:include name='widget-title'/>
                <div class='widget-content'>
                  <data:content/>
                </div>
              </b:includable>
    </b:widget>
  </b:section>
 <div class='clearfix'/>
<!-- Footer Wrapper -->
<div id='footer-wrapper'> 
<div id='sub-footer-wrapper'>
  <div class='container row'>
    <b:section class='menu-footer' id='menu-footer' maxwidgets='1' name='Menu Footer' showaddelement='yes'>
      <b:widget id='LinkList76' locked='true' title='Menu Footer Widget' type='LinkList' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='shownum'>2</b:widget-setting>
          <b:widget-setting name='sorting'>NONE</b:widget-setting>
          <b:widget-setting name='text-1'><![CDATA[<i class="ri-file-user-line"></i>About]]></b:widget-setting>
          <b:widget-setting name='link-1'>https://whocx.com</b:widget-setting>
          <b:widget-setting name='text-0'><![CDATA[<i class="ri-home-8-line"></i>Home]]></b:widget-setting>
          <b:widget-setting name='link-2'><![CDATA[https://href="tel:+18044042557">+18044042557</a></p>]]></b:widget-setting>
          <b:widget-setting name='link-0'>/</b:widget-setting>
          <b:widget-setting name='text-2'><![CDATA[<i class="ri-phone-line"></i>Contact]]></b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
        <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
      </b:widget>
    </b:section>
    <p style='text-align:left;'>Copyright &#169; 2023 <a href='https://www.whocx.com/'>WHO CX.</a> All Right Reseved</p>
<div class='ty-copy-container row' style='font-size:1px; opacity:0;'>
    <div class='copyright-area'>Created By <a href='http://soratemplates.com/' id='mycontent' rel='dofollow' title='SoraTemplates'>Blogger Theme</a> | Distributed By <a href='https://gooyaabitemplates.com/' rel='dofollow' style='color:#ff00ba;' target='_blank' title='Gooyaabi Templates'>Gooyaabi Templates</a>
    </div>
  </div>
  </div>
</div>
</div>
<div class='mobile-foot-menu'>
  <div class='mobile-foot-menu-wrapper'>
    <span class='mobile-foot-menu-home'><a expr:href='data:blog.homepageUrl'/></span>
    <span class='mobile-foot-menu-search'/>
    <span class='mobile-foot-menu-menu'/>
    <span class='mobile-foot-menu-dark'/>
    <span class='mobile-foot-menu-top'/>
  </div>
  </div>
  </div>

<b:if cond='data:view.isSingleItem'>
<!-- Hidden Widgets -->
<div id='hidden-widgets-wrap' style='display:none'>
  <b:section class='hidden-widgets' deleted='true' id='hidden-widgets' maxwidgets='1' showaddelement='no'>
    <b:widget id='ContactForm1' locked='false' title='Contact form' type='ContactForm' visible='true'>
      <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
      <b:includable id='content'>
      <b:include name='contact-form-content'/>
    </b:includable>
    </b:widget>
  </b:section>
</div>
</b:if>
  
<div class='overlay'/>
  <div class='full-screen-search'>
    <div class='mobile-search'>
      <form class='search-form' expr:action='data:blog.searchUrl' role='search'>
        <input autocomplete='off' class='search-input' expr:placeholder='data:messages.search' name='q' type='search' value=''/>
        <button class='search-action' type='submit' value=''/>
      </form>
    </div>
  </div>
  <div class='searchlay'/>
<!-- Main Scripts -->
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js' type='text/javascript'/>
<script type='text/javascript'>
//<![CDATA[   
/*! Owl carousel by Bartosz Wojciechowski/David Deutsch | v2.0.0 - http://owlcarousel2.github.io/OwlCarousel2 */
!function(a,b,c,d){function e(b,c){this.settings=null,this.options=a.extend({},e.Defaults,c),this.$element=a(b),this.drag=a.extend({},m),this.state=a.extend({},n),this.e=a.extend({},o),this._plugins={},this._supress={},this._current=null,this._speed=null,this._coordinates=[],this._breakpoint=null,this._width=null,this._items=[],this._clones=[],this._mergers=[],this._invalidated={},this._pipe=[],a.each(e.Plugins,a.proxy(function(a,b){this._plugins[a[0].toLowerCase()+a.slice(1)]=new b(this)},this)),a.each(e.Pipe,a.proxy(function(b,c){this._pipe.push({filter:c.filter,run:a.proxy(c.run,this)})},this)),this.setup(),this.initialize()}function f(a){if(a.touches!==d)return{x:a.touches[0].pageX,y:a.touches[0].pageY};if(a.touches===d){if(a.pageX!==d)return{x:a.pageX,y:a.pageY};if(a.pageX===d)return{x:a.clientX,y:a.clientY}}}function g(a){var b,d,e=c.createElement("div"),f=a;for(b in f)if(d=f[b],"undefined"!=typeof e.style[d])return e=null,[d,b];return[!1]}function h(){return g(["transition","WebkitTransition","MozTransition","OTransition"])[1]}function i(){return g(["transform","WebkitTransform","MozTransform","OTransform","msTransform"])[0]}function j(){return g(["perspective","webkitPerspective","MozPerspective","OPerspective","MsPerspective"])[0]}function k(){return"ontouchstart"in b||!!navigator.msMaxTouchPoints}function l(){return b.navigator.msPointerEnabled}var m,n,o;m={start:0,startX:0,startY:0,current:0,currentX:0,currentY:0,offsetX:0,offsetY:0,distance:null,startTime:0,endTime:0,updatedX:0,targetEl:null},n={isTouch:!1,isScrolling:!1,isSwiping:!1,direction:!1,inMotion:!1},o={_onDragStart:null,_onDragMove:null,_onDragEnd:null,_transitionEnd:null,_resizer:null,_responsiveCall:null,_goToLoop:null,_checkVisibile:null},e.Defaults={items:3,loop:!1,center:!1,mouseDrag:!0,touchDrag:!0,pullDrag:!0,freeDrag:!1,margin:0,stagePadding:0,merge:!1,mergeFit:!0,autoWidth:!1,startPosition:0,rtl:!1,smartSpeed:250,fluidSpeed:!1,dragEndSpeed:!1,responsive:{},responsiveRefreshRate:200,responsiveBaseElement:b,responsiveClass:!1,fallbackEasing:"swing",info:!1,nestedItemSelector:!1,itemElement:"div",stageElement:"div",themeClass:"owl-theme",baseClass:"owl-carousel",itemClass:"owl-item",centerClass:"center",activeClass:"active"},e.Width={Default:"default",Inner:"inner",Outer:"outer"},e.Plugins={},e.Pipe=[{filter:["width","items","settings"],run:function(a){a.current=this._items&&this._items[this.relative(this._current)]}},{filter:["items","settings"],run:function(){var a=this._clones,b=this.$stage.children(".cloned");(b.length!==a.length||!this.settings.loop&&a.length>0)&&(this.$stage.children(".cloned").remove(),this._clones=[])}},{filter:["items","settings"],run:function(){var a,b,c=this._clones,d=this._items,e=this.settings.loop?c.length-Math.max(2*this.settings.items,4):0;for(a=0,b=Math.abs(e/2);b>a;a++)e>0?(this.$stage.children().eq(d.length+c.length-1).remove(),c.pop(),this.$stage.children().eq(0).remove(),c.pop()):(c.push(c.length/2),this.$stage.append(d[c[c.length-1]].clone().addClass("cloned")),c.push(d.length-1-(c.length-1)/2),this.$stage.prepend(d[c[c.length-1]].clone().addClass("cloned")))}},{filter:["width","items","settings"],run:function(){var a,b,c,d=this.settings.rtl?1:-1,e=(this.width()/this.settings.items).toFixed(3),f=0;for(this._coordinates=[],b=0,c=this._clones.length+this._items.length;c>b;b++)a=this._mergers[this.relative(b)],a=this.settings.mergeFit&&Math.min(a,this.settings.items)||a,f+=(this.settings.autoWidth?this._items[this.relative(b)].width()+this.settings.margin:e*a)*d,this._coordinates.push(f)}},{filter:["width","items","settings"],run:function(){var b,c,d=(this.width()/this.settings.items).toFixed(3),e={width:Math.abs(this._coordinates[this._coordinates.length-1])+2*this.settings.stagePadding,"padding-left":this.settings.stagePadding||"","padding-right":this.settings.stagePadding||""};if(this.$stage.css(e),e={width:this.settings.autoWidth?"auto":d-this.settings.margin},e[this.settings.rtl?"margin-left":"margin-right"]=this.settings.margin,!this.settings.autoWidth&&a.grep(this._mergers,function(a){return a>1}).length>0)for(b=0,c=this._coordinates.length;c>b;b++)e.width=Math.abs(this._coordinates[b])-Math.abs(this._coordinates[b-1]||0)-this.settings.margin,this.$stage.children().eq(b).css(e);else this.$stage.children().css(e)}},{filter:["width","items","settings"],run:function(a){a.current&&this.reset(this.$stage.children().index(a.current))}},{filter:["position"],run:function(){this.animate(this.coordinates(this._current))}},{filter:["width","position","items","settings"],run:function(){var a,b,c,d,e=this.settings.rtl?1:-1,f=2*this.settings.stagePadding,g=this.coordinates(this.current())+f,h=g+this.width()*e,i=[];for(c=0,d=this._coordinates.length;d>c;c++)a=this._coordinates[c-1]||0,b=Math.abs(this._coordinates[c])+f*e,(this.op(a,"<=",g)&&this.op(a,">",h)||this.op(b,"<",g)&&this.op(b,">",h))&&i.push(c);this.$stage.children("."+this.settings.activeClass).removeClass(this.settings.activeClass),this.$stage.children(":eq("+i.join("), :eq(")+")").addClass(this.settings.activeClass),this.settings.center&&(this.$stage.children("."+this.settings.centerClass).removeClass(this.settings.centerClass),this.$stage.children().eq(this.current()).addClass(this.settings.centerClass))}}],e.prototype.initialize=function(){if(this.trigger("initialize"),this.$element.addClass(this.settings.baseClass).addClass(this.settings.themeClass).toggleClass("owl-rtl",this.settings.rtl),this.browserSupport(),this.settings.autoWidth&&this.state.imagesLoaded!==!0){var b,c,e;if(b=this.$element.find("img"),c=this.settings.nestedItemSelector?"."+this.settings.nestedItemSelector:d,e=this.$element.children(c).width(),b.length&&0>=e)return this.preloadAutoWidthImages(b),!1}this.$element.addClass("owl-loading"),this.$stage=a("<"+this.settings.stageElement+' class="owl-stage"/>').wrap('<div class="owl-stage-outer">'),this.$element.append(this.$stage.parent()),this.replace(this.$element.children().not(this.$stage.parent())),this._width=this.$element.width(),this.refresh(),this.$element.removeClass("owl-loading").addClass("owl-loaded"),this.eventsCall(),this.internalEvents(),this.addTriggerableEvents(),this.trigger("initialized")},e.prototype.setup=function(){var b=this.viewport(),c=this.options.responsive,d=-1,e=null;c?(a.each(c,function(a){b>=a&&a>d&&(d=Number(a))}),e=a.extend({},this.options,c[d]),delete e.responsive,e.responsiveClass&&this.$element.attr("class",function(a,b){return b.replace(/\b owl-responsive-\S+/g,"")}).addClass("owl-responsive-"+d)):e=a.extend({},this.options),(null===this.settings||this._breakpoint!==d)&&(this.trigger("change",{property:{name:"settings",value:e}}),this._breakpoint=d,this.settings=e,this.invalidate("settings"),this.trigger("changed",{property:{name:"settings",value:this.settings}}))},e.prototype.optionsLogic=function(){this.$element.toggleClass("owl-center",this.settings.center),this.settings.loop&&this._items.length<this.settings.items&&(this.settings.loop=!1),this.settings.autoWidth&&(this.settings.stagePadding=!1,this.settings.merge=!1)},e.prototype.prepare=function(b){var c=this.trigger("prepare",{content:b});return c.data||(c.data=a("<"+this.settings.itemElement+"/>").addClass(this.settings.itemClass).append(b)),this.trigger("prepared",{content:c.data}),c.data},e.prototype.update=function(){for(var b=0,c=this._pipe.length,d=a.proxy(function(a){return this[a]},this._invalidated),e={};c>b;)(this._invalidated.all||a.grep(this._pipe[b].filter,d).length>0)&&this._pipe[b].run(e),b++;this._invalidated={}},e.prototype.width=function(a){switch(a=a||e.Width.Default){case e.Width.Inner:case e.Width.Outer:return this._width;default:return this._width-2*this.settings.stagePadding+this.settings.margin}},e.prototype.refresh=function(){if(0===this._items.length)return!1;(new Date).getTime();this.trigger("refresh"),this.setup(),this.optionsLogic(),this.$stage.addClass("owl-refresh"),this.update(),this.$stage.removeClass("owl-refresh"),this.state.orientation=b.orientation,this.watchVisibility(),this.trigger("refreshed")},e.prototype.eventsCall=function(){this.e._onDragStart=a.proxy(function(a){this.onDragStart(a)},this),this.e._onDragMove=a.proxy(function(a){this.onDragMove(a)},this),this.e._onDragEnd=a.proxy(function(a){this.onDragEnd(a)},this),this.e._onResize=a.proxy(function(a){this.onResize(a)},this),this.e._transitionEnd=a.proxy(function(a){this.transitionEnd(a)},this),this.e._preventClick=a.proxy(function(a){this.preventClick(a)},this)},e.prototype.onThrottledResize=function(){b.clearTimeout(this.resizeTimer),this.resizeTimer=b.setTimeout(this.e._onResize,this.settings.responsiveRefreshRate)},e.prototype.onResize=function(){return this._items.length?this._width===this.$element.width()?!1:this.trigger("resize").isDefaultPrevented()?!1:(this._width=this.$element.width(),this.invalidate("width"),this.refresh(),void this.trigger("resized")):!1},e.prototype.eventsRouter=function(a){var b=a.type;"mousedown"===b||"touchstart"===b?this.onDragStart(a):"mousemove"===b||"touchmove"===b?this.onDragMove(a):"mouseup"===b||"touchend"===b?this.onDragEnd(a):"touchcancel"===b&&this.onDragEnd(a)},e.prototype.internalEvents=function(){var c=(k(),l());this.settings.mouseDrag?(this.$stage.on("mousedown",a.proxy(function(a){this.eventsRouter(a)},this)),this.$stage.on("dragstart",function(){return!1}),this.$stage.get(0).onselectstart=function(){return!1}):this.$element.addClass("owl-text-select-on"),this.settings.touchDrag&&!c&&this.$stage.on("touchstart touchcancel",a.proxy(function(a){this.eventsRouter(a)},this)),this.transitionEndVendor&&this.on(this.$stage.get(0),this.transitionEndVendor,this.e._transitionEnd,!1),this.settings.responsive!==!1&&this.on(b,"resize",a.proxy(this.onThrottledResize,this))},e.prototype.onDragStart=function(d){var e,g,h,i;if(e=d.originalEvent||d||b.event,3===e.which||this.state.isTouch)return!1;if("mousedown"===e.type&&this.$stage.addClass("owl-grab"),this.trigger("drag"),this.drag.startTime=(new Date).getTime(),this.speed(0),this.state.isTouch=!0,this.state.isScrolling=!1,this.state.isSwiping=!1,this.drag.distance=0,g=f(e).x,h=f(e).y,this.drag.offsetX=this.$stage.position().left,this.drag.offsetY=this.$stage.position().top,this.settings.rtl&&(this.drag.offsetX=this.$stage.position().left+this.$stage.width()-this.width()+this.settings.margin),this.state.inMotion&&this.support3d)i=this.getTransformProperty(),this.drag.offsetX=i,this.animate(i),this.state.inMotion=!0;else if(this.state.inMotion&&!this.support3d)return this.state.inMotion=!1,!1;this.drag.startX=g-this.drag.offsetX,this.drag.startY=h-this.drag.offsetY,this.drag.start=g-this.drag.startX,this.drag.targetEl=e.target||e.srcElement,this.drag.updatedX=this.drag.start,("IMG"===this.drag.targetEl.tagName||"A"===this.drag.targetEl.tagName)&&(this.drag.targetEl.draggable=!1),a(c).on("mousemove.owl.dragEvents mouseup.owl.dragEvents touchmove.owl.dragEvents touchend.owl.dragEvents",a.proxy(function(a){this.eventsRouter(a)},this))},e.prototype.onDragMove=function(a){var c,e,g,h,i,j;this.state.isTouch&&(this.state.isScrolling||(c=a.originalEvent||a||b.event,e=f(c).x,g=f(c).y,this.drag.currentX=e-this.drag.startX,this.drag.currentY=g-this.drag.startY,this.drag.distance=this.drag.currentX-this.drag.offsetX,this.drag.distance<0?this.state.direction=this.settings.rtl?"right":"left":this.drag.distance>0&&(this.state.direction=this.settings.rtl?"left":"right"),this.settings.loop?this.op(this.drag.currentX,">",this.coordinates(this.minimum()))&&"right"===this.state.direction?this.drag.currentX-=(this.settings.center&&this.coordinates(0))-this.coordinates(this._items.length):this.op(this.drag.currentX,"<",this.coordinates(this.maximum()))&&"left"===this.state.direction&&(this.drag.currentX+=(this.settings.center&&this.coordinates(0))-this.coordinates(this._items.length)):(h=this.coordinates(this.settings.rtl?this.maximum():this.minimum()),i=this.coordinates(this.settings.rtl?this.minimum():this.maximum()),j=this.settings.pullDrag?this.drag.distance/5:0,this.drag.currentX=Math.max(Math.min(this.drag.currentX,h+j),i+j)),(this.drag.distance>8||this.drag.distance<-8)&&(c.preventDefault!==d?c.preventDefault():c.returnValue=!1,this.state.isSwiping=!0),this.drag.updatedX=this.drag.currentX,(this.drag.currentY>16||this.drag.currentY<-16)&&this.state.isSwiping===!1&&(this.state.isScrolling=!0,this.drag.updatedX=this.drag.start),this.animate(this.drag.updatedX)))},e.prototype.onDragEnd=function(b){var d,e,f;if(this.state.isTouch){if("mouseup"===b.type&&this.$stage.removeClass("owl-grab"),this.trigger("dragged"),this.drag.targetEl.removeAttribute("draggable"),this.state.isTouch=!1,this.state.isScrolling=!1,this.state.isSwiping=!1,0===this.drag.distance&&this.state.inMotion!==!0)return this.state.inMotion=!1,!1;this.drag.endTime=(new Date).getTime(),d=this.drag.endTime-this.drag.startTime,e=Math.abs(this.drag.distance),(e>3||d>300)&&this.removeClick(this.drag.targetEl),f=this.closest(this.drag.updatedX),this.speed(this.settings.dragEndSpeed||this.settings.smartSpeed),this.current(f),this.invalidate("position"),this.update(),this.settings.pullDrag||this.drag.updatedX!==this.coordinates(f)||this.transitionEnd(),this.drag.distance=0,a(c).off(".owl.dragEvents")}},e.prototype.removeClick=function(c){this.drag.targetEl=c,a(c).on("click.preventClick",this.e._preventClick),b.setTimeout(function(){a(c).off("click.preventClick")},300)},e.prototype.preventClick=function(b){b.preventDefault?b.preventDefault():b.returnValue=!1,b.stopPropagation&&b.stopPropagation(),a(b.target).off("click.preventClick")},e.prototype.getTransformProperty=function(){var a,c;return a=b.getComputedStyle(this.$stage.get(0),null).getPropertyValue(this.vendorName+"transform"),a=a.replace(/matrix(3d)?\(|\)/g,"").split(","),c=16===a.length,c!==!0?a[4]:a[12]},e.prototype.closest=function(b){var c=-1,d=30,e=this.width(),f=this.coordinates();return this.settings.freeDrag||a.each(f,a.proxy(function(a,g){return b>g-d&&g+d>b?c=a:this.op(b,"<",g)&&this.op(b,">",f[a+1]||g-e)&&(c="left"===this.state.direction?a+1:a),-1===c},this)),this.settings.loop||(this.op(b,">",f[this.minimum()])?c=b=this.minimum():this.op(b,"<",f[this.maximum()])&&(c=b=this.maximum())),c},e.prototype.animate=function(b){this.trigger("translate"),this.state.inMotion=this.speed()>0,this.support3d?this.$stage.css({transform:"translate3d("+b+"px,0px, 0px)",transition:this.speed()/1e3+"s"}):this.state.isTouch?this.$stage.css({left:b+"px"}):this.$stage.animate({left:b},this.speed()/1e3,this.settings.fallbackEasing,a.proxy(function(){this.state.inMotion&&this.transitionEnd()},this))},e.prototype.current=function(a){if(a===d)return this._current;if(0===this._items.length)return d;if(a=this.normalize(a),this._current!==a){var b=this.trigger("change",{property:{name:"position",value:a}});b.data!==d&&(a=this.normalize(b.data)),this._current=a,this.invalidate("position"),this.trigger("changed",{property:{name:"position",value:this._current}})}return this._current},e.prototype.invalidate=function(a){this._invalidated[a]=!0},e.prototype.reset=function(a){a=this.normalize(a),a!==d&&(this._speed=0,this._current=a,this.suppress(["translate","translated"]),this.animate(this.coordinates(a)),this.release(["translate","translated"]))},e.prototype.normalize=function(b,c){var e=c?this._items.length:this._items.length+this._clones.length;return!a.isNumeric(b)||1>e?d:b=this._clones.length?(b%e+e)%e:Math.max(this.minimum(c),Math.min(this.maximum(c),b))},e.prototype.relative=function(a){return a=this.normalize(a),a-=this._clones.length/2,this.normalize(a,!0)},e.prototype.maximum=function(a){var b,c,d,e=0,f=this.settings;if(a)return this._items.length-1;if(!f.loop&&f.center)b=this._items.length-1;else if(f.loop||f.center)if(f.loop||f.center)b=this._items.length+f.items;else{if(!f.autoWidth&&!f.merge)throw"Can not detect maximum absolute position.";for(revert=f.rtl?1:-1,c=this.$stage.width()-this.$element.width();(d=this.coordinates(e))&&!(d*revert>=c);)b=++e}else b=this._items.length-f.items;return b},e.prototype.minimum=function(a){return a?0:this._clones.length/2},e.prototype.items=function(a){return a===d?this._items.slice():(a=this.normalize(a,!0),this._items[a])},e.prototype.mergers=function(a){return a===d?this._mergers.slice():(a=this.normalize(a,!0),this._mergers[a])},e.prototype.clones=function(b){var c=this._clones.length/2,e=c+this._items.length,f=function(a){return a%2===0?e+a/2:c-(a+1)/2};return b===d?a.map(this._clones,function(a,b){return f(b)}):a.map(this._clones,function(a,c){return a===b?f(c):null})},e.prototype.speed=function(a){return a!==d&&(this._speed=a),this._speed},e.prototype.coordinates=function(b){var c=null;return b===d?a.map(this._coordinates,a.proxy(function(a,b){return this.coordinates(b)},this)):(this.settings.center?(c=this._coordinates[b],c+=(this.width()-c+(this._coordinates[b-1]||0))/2*(this.settings.rtl?-1:1)):c=this._coordinates[b-1]||0,c)},e.prototype.duration=function(a,b,c){return Math.min(Math.max(Math.abs(b-a),1),6)*Math.abs(c||this.settings.smartSpeed)},e.prototype.to=function(c,d){if(this.settings.loop){var e=c-this.relative(this.current()),f=this.current(),g=this.current(),h=this.current()+e,i=0>g-h?!0:!1,j=this._clones.length+this._items.length;h<this.settings.items&&i===!1?(f=g+this._items.length,this.reset(f)):h>=j-this.settings.items&&i===!0&&(f=g-this._items.length,this.reset(f)),b.clearTimeout(this.e._goToLoop),this.e._goToLoop=b.setTimeout(a.proxy(function(){this.speed(this.duration(this.current(),f+e,d)),this.current(f+e),this.update()},this),30)}else this.speed(this.duration(this.current(),c,d)),this.current(c),this.update()},e.prototype.next=function(a){a=a||!1,this.to(this.relative(this.current())+1,a)},e.prototype.prev=function(a){a=a||!1,this.to(this.relative(this.current())-1,a)},e.prototype.transitionEnd=function(a){return a!==d&&(a.stopPropagation(),(a.target||a.srcElement||a.originalTarget)!==this.$stage.get(0))?!1:(this.state.inMotion=!1,void this.trigger("translated"))},e.prototype.viewport=function(){var d;if(this.options.responsiveBaseElement!==b)d=a(this.options.responsiveBaseElement).width();else if(b.innerWidth)d=b.innerWidth;else{if(!c.documentElement||!c.documentElement.clientWidth)throw"Can not detect viewport width.";d=c.documentElement.clientWidth}return d},e.prototype.replace=function(b){this.$stage.empty(),this._items=[],b&&(b=b instanceof jQuery?b:a(b)),this.settings.nestedItemSelector&&(b=b.find("."+this.settings.nestedItemSelector)),b.filter(function(){return 1===this.nodeType}).each(a.proxy(function(a,b){b=this.prepare(b),this.$stage.append(b),this._items.push(b),this._mergers.push(1*b.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)},this)),this.reset(a.isNumeric(this.settings.startPosition)?this.settings.startPosition:0),this.invalidate("items")},e.prototype.add=function(a,b){b=b===d?this._items.length:this.normalize(b,!0),this.trigger("add",{content:a,position:b}),0===this._items.length||b===this._items.length?(this.$stage.append(a),this._items.push(a),this._mergers.push(1*a.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)):(this._items[b].before(a),this._items.splice(b,0,a),this._mergers.splice(b,0,1*a.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)),this.invalidate("items"),this.trigger("added",{content:a,position:b})},e.prototype.remove=function(a){a=this.normalize(a,!0),a!==d&&(this.trigger("remove",{content:this._items[a],position:a}),this._items[a].remove(),this._items.splice(a,1),this._mergers.splice(a,1),this.invalidate("items"),this.trigger("removed",{content:null,position:a}))},e.prototype.addTriggerableEvents=function(){var b=a.proxy(function(b,c){return a.proxy(function(a){a.relatedTarget!==this&&(this.suppress([c]),b.apply(this,[].slice.call(arguments,1)),this.release([c]))},this)},this);a.each({next:this.next,prev:this.prev,to:this.to,destroy:this.destroy,refresh:this.refresh,replace:this.replace,add:this.add,remove:this.remove},a.proxy(function(a,c){this.$element.on(a+".owl.carousel",b(c,a+".owl.carousel"))},this))},e.prototype.watchVisibility=function(){function c(a){return a.offsetWidth>0&&a.offsetHeight>0}function d(){c(this.$element.get(0))&&(this.$element.removeClass("owl-hidden"),this.refresh(),b.clearInterval(this.e._checkVisibile))}c(this.$element.get(0))||(this.$element.addClass("owl-hidden"),b.clearInterval(this.e._checkVisibile),this.e._checkVisibile=b.setInterval(a.proxy(d,this),500))},e.prototype.preloadAutoWidthImages=function(b){var c,d,e,f;c=0,d=this,b.each(function(g,h){e=a(h),f=new Image,f.onload=function(){c++,e.attr("src",f.src),e.css("opacity",1),c>=b.length&&(d.state.imagesLoaded=!0,d.initialize())},f.src=e.attr("src")||e.attr("data-src")||e.attr("data-src-retina")})},e.prototype.destroy=function(){this.$element.hasClass(this.settings.themeClass)&&this.$element.removeClass(this.settings.themeClass),this.settings.responsive!==!1&&a(b).off("resize.owl.carousel"),this.transitionEndVendor&&this.off(this.$stage.get(0),this.transitionEndVendor,this.e._transitionEnd);for(var d in this._plugins)this._plugins[d].destroy();(this.settings.mouseDrag||this.settings.touchDrag)&&(this.$stage.off("mousedown touchstart touchcancel"),a(c).off(".owl.dragEvents"),this.$stage.get(0).onselectstart=function(){},this.$stage.off("dragstart",function(){return!1})),this.$element.off(".owl"),this.$stage.children(".cloned").remove(),this.e=null,this.$element.removeData("owlCarousel"),this.$stage.children().contents().unwrap(),this.$stage.children().unwrap(),this.$stage.unwrap()},e.prototype.op=function(a,b,c){var d=this.settings.rtl;switch(b){case"<":return d?a>c:c>a;case">":return d?c>a:a>c;case">=":return d?c>=a:a>=c;case"<=":return d?a>=c:c>=a}},e.prototype.on=function(a,b,c,d){a.addEventListener?a.addEventListener(b,c,d):a.attachEvent&&a.attachEvent("on"+b,c)},e.prototype.off=function(a,b,c,d){a.removeEventListener?a.removeEventListener(b,c,d):a.detachEvent&&a.detachEvent("on"+b,c)},e.prototype.trigger=function(b,c,d){var e={item:{count:this._items.length,index:this.current()}},f=a.camelCase(a.grep(["on",b,d],function(a){return a}).join("-").toLowerCase()),g=a.Event([b,"owl",d||"carousel"].join(".").toLowerCase(),a.extend({relatedTarget:this},e,c));return this._supress[b]||(a.each(this._plugins,function(a,b){b.onTrigger&&b.onTrigger(g)}),this.$element.trigger(g),this.settings&&"function"==typeof this.settings[f]&&this.settings[f].apply(this,g)),g},e.prototype.suppress=function(b){a.each(b,a.proxy(function(a,b){this._supress[b]=!0},this))},e.prototype.release=function(b){a.each(b,a.proxy(function(a,b){delete this._supress[b]},this))},e.prototype.browserSupport=function(){if(this.support3d=j(),this.support3d){this.transformVendor=i();var a=["transitionend","webkitTransitionEnd","transitionend","oTransitionEnd"];this.transitionEndVendor=a[h()],this.vendorName=this.transformVendor.replace(/Transform/i,""),this.vendorName=""!==this.vendorName?"-"+this.vendorName.toLowerCase()+"-":""}this.state.orientation=b.orientation},a.fn.owlCarousel=function(b){return this.each(function(){a(this).data("owlCarousel")||a(this).data("owlCarousel",new e(this,b))})},a.fn.owlCarousel.Constructor=e}(window.Zepto||window.jQuery,window,document),function(a,b){var c=function(b){this._core=b,this._loaded=[],this._handlers={"initialized.owl.carousel change.owl.carousel":a.proxy(function(b){if(b.namespace&&this._core.settings&&this._core.settings.lazyLoad&&(b.property&&"position"==b.property.name||"initialized"==b.type))for(var c=this._core.settings,d=c.center&&Math.ceil(c.items/2)||c.items,e=c.center&&-1*d||0,f=(b.property&&b.property.value||this._core.current())+e,g=this._core.clones().length,h=a.proxy(function(a,b){this.load(b)},this);e++<d;)this.load(g/2+this._core.relative(f)),g&&a.each(this._core.clones(this._core.relative(f++)),h)},this)},this._core.options=a.extend({},c.Defaults,this._core.options),this._core.$element.on(this._handlers)};c.Defaults={lazyLoad:!1},c.prototype.load=function(c){var d=this._core.$stage.children().eq(c),e=d&&d.find(".owl-lazy");!e||a.inArray(d.get(0),this._loaded)>-1||(e.each(a.proxy(function(c,d){var e,f=a(d),g=b.devicePixelRatio>1&&f.attr("data-src-retina")||f.attr("data-src");this._core.trigger("load",{element:f,url:g},"lazy"),f.is("img")?f.one("load.owl.lazy",a.proxy(function(){f.css("opacity",1),this._core.trigger("loaded",{element:f,url:g},"lazy")},this)).attr("src",g):(e=new Image,e.onload=a.proxy(function(){f.css({"background-image":"url("+g+")",opacity:"1"}),this._core.trigger("loaded",{element:f,url:g},"lazy")},this),e.src=g)},this)),this._loaded.push(d.get(0)))},c.prototype.destroy=function(){var a,b;for(a in this.handlers)this._core.$element.off(a,this.handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Lazy=c}(window.Zepto||window.jQuery,window,document),function(a){var b=function(c){this._core=c,this._handlers={"initialized.owl.carousel":a.proxy(function(){this._core.settings.autoHeight&&this.update()},this),"changed.owl.carousel":a.proxy(function(a){this._core.settings.autoHeight&&"position"==a.property.name&&this.update()},this),"loaded.owl.lazy":a.proxy(function(a){this._core.settings.autoHeight&&a.element.closest("."+this._core.settings.itemClass)===this._core.$stage.children().eq(this._core.current())&&this.update()},this)},this._core.options=a.extend({},b.Defaults,this._core.options),this._core.$element.on(this._handlers)};b.Defaults={autoHeight:!1,autoHeightClass:"owl-height"},b.prototype.update=function(){this._core.$stage.parent().height(this._core.$stage.children().eq(this._core.current()).height()).addClass(this._core.settings.autoHeightClass)},b.prototype.destroy=function(){var a,b;for(a in this._handlers)this._core.$element.off(a,this._handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.AutoHeight=b}(window.Zepto||window.jQuery,window,document),function(a,b,c){var d=function(b){this._core=b,this._videos={},this._playing=null,this._fullscreen=!1,this._handlers={"resize.owl.carousel":a.proxy(function(a){this._core.settings.video&&!this.isInFullScreen()&&a.preventDefault()},this),"refresh.owl.carousel changed.owl.carousel":a.proxy(function(){this._playing&&this.stop()},this),"prepared.owl.carousel":a.proxy(function(b){var c=a(b.content).find(".owl-video");c.length&&(c.css("display","none"),this.fetch(c,a(b.content)))},this)},this._core.options=a.extend({},d.Defaults,this._core.options),this._core.$element.on(this._handlers),this._core.$element.on("click.owl.video",".owl-video-play-icon",a.proxy(function(a){this.play(a)},this))};d.Defaults={video:!1,videoHeight:!1,videoWidth:!1},d.prototype.fetch=function(a,b){var c=a.attr("data-vimeo-id")?"vimeo":"youtube",d=a.attr("data-vimeo-id")||a.attr("data-youtube-id"),e=a.attr("data-width")||this._core.settings.videoWidth,f=a.attr("data-height")||this._core.settings.videoHeight,g=a.attr("href");if(!g)throw new Error("Missing video URL.");if(d=g.match(/(http:|https:|)\/\/(player.|www.)?(vimeo\.com|youtu(be\.com|\.be|be\.googleapis\.com))\/(video\/|embed\/|watch\?v=|v\/)?([A-Za-z0-9._%-]*)(\&\S+)?/),d[3].indexOf("youtu")>-1)c="youtube";else{if(!(d[3].indexOf("vimeo")>-1))throw new Error("Video URL not supported.");c="vimeo"}d=d[6],this._videos[g]={type:c,id:d,width:e,height:f},b.attr("data-video",g),this.thumbnail(a,this._videos[g])},d.prototype.thumbnail=function(b,c){var d,e,f,g=c.width&&c.height?'style="width:'+c.width+"px;height:"+c.height+'px;"':"",h=b.find("img"),i="src",j="",k=this._core.settings,l=function(a){e='<div class="owl-video-play-icon"></div>',d=k.lazyLoad?'<div class="owl-video-tn '+j+'" '+i+'="'+a+'"></div>':'<div class="owl-video-tn" style="opacity:1;background-image:url('+a+')"></div>',b.after(d),b.after(e)};return b.wrap('<div class="owl-video-wrapper"'+g+"></div>"),this._core.settings.lazyLoad&&(i="data-src",j="owl-lazy"),h.length?(l(h.attr(i)),h.remove(),!1):void("youtube"===c.type?(f="http://img.youtube.com/vi/"+c.id+"/hqdefault.jpg",l(f)):"vimeo"===c.type&&a.ajax({type:"GET",url:"http://vimeo.com/api/v2/video/"+c.id+".json",jsonp:"callback",dataType:"jsonp",success:function(a){f=a[0].thumbnail_large,l(f)}}))},d.prototype.stop=function(){this._core.trigger("stop",null,"video"),this._playing.find(".owl-video-frame").remove(),this._playing.removeClass("owl-video-playing"),this._playing=null},d.prototype.play=function(b){this._core.trigger("play",null,"video"),this._playing&&this.stop();var c,d,e=a(b.target||b.srcElement),f=e.closest("."+this._core.settings.itemClass),g=this._videos[f.attr("data-video")],h=g.width||"100%",i=g.height||this._core.$stage.height();"youtube"===g.type?c='<iframe width="'+h+'" height="'+i+'" src="http://www.youtube.com/embed/'+g.id+"?autoplay=1&v="+g.id+'" frameborder="0" allowfullscreen></iframe>':"vimeo"===g.type&&(c='<iframe src="http://player.vimeo.com/video/'+g.id+'?autoplay=1" width="'+h+'" height="'+i+'" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>'),f.addClass("owl-video-playing"),this._playing=f,d=a('<div style="height:'+i+"px; width:"+h+'px" class="owl-video-frame">'+c+"</div>"),e.after(d)},d.prototype.isInFullScreen=function(){var d=c.fullscreenElement||c.mozFullScreenElement||c.webkitFullscreenElement;return d&&a(d).parent().hasClass("owl-video-frame")&&(this._core.speed(0),this._fullscreen=!0),d&&this._fullscreen&&this._playing?!1:this._fullscreen?(this._fullscreen=!1,!1):this._playing&&this._core.state.orientation!==b.orientation?(this._core.state.orientation=b.orientation,!1):!0},d.prototype.destroy=function(){var a,b;this._core.$element.off("click.owl.video");for(a in this._handlers)this._core.$element.off(a,this._handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Video=d}(window.Zepto||window.jQuery,window,document),function(a,b,c,d){var e=function(b){this.core=b,this.core.options=a.extend({},e.Defaults,this.core.options),this.swapping=!0,this.previous=d,this.next=d,this.handlers={"change.owl.carousel":a.proxy(function(a){"position"==a.property.name&&(this.previous=this.core.current(),this.next=a.property.value)},this),"drag.owl.carousel dragged.owl.carousel translated.owl.carousel":a.proxy(function(a){this.swapping="translated"==a.type},this),"translate.owl.carousel":a.proxy(function(){this.swapping&&(this.core.options.animateOut||this.core.options.animateIn)&&this.swap()},this)},this.core.$element.on(this.handlers)};e.Defaults={animateOut:!1,animateIn:!1},e.prototype.swap=function(){if(1===this.core.settings.items&&this.core.support3d){this.core.speed(0);var b,c=a.proxy(this.clear,this),d=this.core.$stage.children().eq(this.previous),e=this.core.$stage.children().eq(this.next),f=this.core.settings.animateIn,g=this.core.settings.animateOut;this.core.current()!==this.previous&&(g&&(b=this.core.coordinates(this.previous)-this.core.coordinates(this.next),d.css({left:b+"px"}).addClass("animated owl-animated-out").addClass(g).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",c)),f&&e.addClass("animated owl-animated-in").addClass(f).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",c))}},e.prototype.clear=function(b){a(b.target).css({left:""}).removeClass("animated owl-animated-out owl-animated-in").removeClass(this.core.settings.animateIn).removeClass(this.core.settings.animateOut),this.core.transitionEnd()},e.prototype.destroy=function(){var a,b;for(a in this.handlers)this.core.$element.off(a,this.handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Animate=e}(window.Zepto||window.jQuery,window,document),function(a,b,c){var d=function(b){this.core=b,this.core.options=a.extend({},d.Defaults,this.core.options),this.handlers={"translated.owl.carousel refreshed.owl.carousel":a.proxy(function(){this.autoplay()
},this),"play.owl.autoplay":a.proxy(function(a,b,c){this.play(b,c)},this),"stop.owl.autoplay":a.proxy(function(){this.stop()},this),"mouseover.owl.autoplay":a.proxy(function(){this.core.settings.autoplayHoverPause&&this.pause()},this),"mouseleave.owl.autoplay":a.proxy(function(){this.core.settings.autoplayHoverPause&&this.autoplay()},this)},this.core.$element.on(this.handlers)};d.Defaults={autoplay:!1,autoplayTimeout:5e3,autoplayHoverPause:!1,autoplaySpeed:!1},d.prototype.autoplay=function(){this.core.settings.autoplay&&!this.core.state.videoPlay?(b.clearInterval(this.interval),this.interval=b.setInterval(a.proxy(function(){this.play()},this),this.core.settings.autoplayTimeout)):b.clearInterval(this.interval)},d.prototype.play=function(){return c.hidden===!0||this.core.state.isTouch||this.core.state.isScrolling||this.core.state.isSwiping||this.core.state.inMotion?void 0:this.core.settings.autoplay===!1?void b.clearInterval(this.interval):void this.core.next(this.core.settings.autoplaySpeed)},d.prototype.stop=function(){b.clearInterval(this.interval)},d.prototype.pause=function(){b.clearInterval(this.interval)},d.prototype.destroy=function(){var a,c;b.clearInterval(this.interval);for(a in this.handlers)this.core.$element.off(a,this.handlers[a]);for(c in Object.getOwnPropertyNames(this))"function"!=typeof this[c]&&(this[c]=null)},a.fn.owlCarousel.Constructor.Plugins.autoplay=d}(window.Zepto||window.jQuery,window,document),function(a){"use strict";var b=function(c){this._core=c,this._initialized=!1,this._pages=[],this._controls={},this._templates=[],this.$element=this._core.$element,this._overrides={next:this._core.next,prev:this._core.prev,to:this._core.to},this._handlers={"prepared.owl.carousel":a.proxy(function(b){this._core.settings.dotsData&&this._templates.push(a(b.content).find("[data-dot]").andSelf("[data-dot]").attr("data-dot"))},this),"add.owl.carousel":a.proxy(function(b){this._core.settings.dotsData&&this._templates.splice(b.position,0,a(b.content).find("[data-dot]").andSelf("[data-dot]").attr("data-dot"))},this),"remove.owl.carousel prepared.owl.carousel":a.proxy(function(a){this._core.settings.dotsData&&this._templates.splice(a.position,1)},this),"change.owl.carousel":a.proxy(function(a){if("position"==a.property.name&&!this._core.state.revert&&!this._core.settings.loop&&this._core.settings.navRewind){var b=this._core.current(),c=this._core.maximum(),d=this._core.minimum();a.data=a.property.value>c?b>=c?d:c:a.property.value<d?c:a.property.value}},this),"changed.owl.carousel":a.proxy(function(a){"position"==a.property.name&&this.draw()},this),"refreshed.owl.carousel":a.proxy(function(){this._initialized||(this.initialize(),this._initialized=!0),this._core.trigger("refresh",null,"navigation"),this.update(),this.draw(),this._core.trigger("refreshed",null,"navigation")},this)},this._core.options=a.extend({},b.Defaults,this._core.options),this.$element.on(this._handlers)};b.Defaults={nav:!1,navRewind:!0,navText:["prev","next"],navSpeed:!1,navElement:"div",navContainer:!1,navContainerClass:"owl-nav",navClass:["owl-prev","owl-next"],slideBy:1,dotClass:"owl-dot",dotsClass:"owl-dots",dots:!0,dotsEach:!1,dotData:!1,dotsSpeed:!1,dotsContainer:!1,controlsClass:"owl-controls"},b.prototype.initialize=function(){var b,c,d=this._core.settings;d.dotsData||(this._templates=[a("<div>").addClass(d.dotClass).append(a("<span>")).prop("outerHTML")]),d.navContainer&&d.dotsContainer||(this._controls.$container=a("<div>").addClass(d.controlsClass).appendTo(this.$element)),this._controls.$indicators=d.dotsContainer?a(d.dotsContainer):a("<div>").hide().addClass(d.dotsClass).appendTo(this._controls.$container),this._controls.$indicators.on("click","div",a.proxy(function(b){var c=a(b.target).parent().is(this._controls.$indicators)?a(b.target).index():a(b.target).parent().index();b.preventDefault(),this.to(c,d.dotsSpeed)},this)),b=d.navContainer?a(d.navContainer):a("<div>").addClass(d.navContainerClass).prependTo(this._controls.$container),this._controls.$next=a("<"+d.navElement+">"),this._controls.$previous=this._controls.$next.clone(),this._controls.$previous.addClass(d.navClass[0]).html(d.navText[0]).hide().prependTo(b).on("click",a.proxy(function(){this.prev(d.navSpeed)},this)),this._controls.$next.addClass(d.navClass[1]).html(d.navText[1]).hide().appendTo(b).on("click",a.proxy(function(){this.next(d.navSpeed)},this));for(c in this._overrides)this._core[c]=a.proxy(this[c],this)},b.prototype.destroy=function(){var a,b,c,d;for(a in this._handlers)this.$element.off(a,this._handlers[a]);for(b in this._controls)this._controls[b].remove();for(d in this.overides)this._core[d]=this._overrides[d];for(c in Object.getOwnPropertyNames(this))"function"!=typeof this[c]&&(this[c]=null)},b.prototype.update=function(){var a,b,c,d=this._core.settings,e=this._core.clones().length/2,f=e+this._core.items().length,g=d.center||d.autoWidth||d.dotData?1:d.dotsEach||d.items;if("page"!==d.slideBy&&(d.slideBy=Math.min(d.slideBy,d.items)),d.dots||"page"==d.slideBy)for(this._pages=[],a=e,b=0,c=0;f>a;a++)(b>=g||0===b)&&(this._pages.push({start:a-e,end:a-e+g-1}),b=0,++c),b+=this._core.mergers(this._core.relative(a))},b.prototype.draw=function(){var b,c,d="",e=this._core.settings,f=(this._core.$stage.children(),this._core.relative(this._core.current()));if(!e.nav||e.loop||e.navRewind||(this._controls.$previous.toggleClass("disabled",0>=f),this._controls.$next.toggleClass("disabled",f>=this._core.maximum())),this._controls.$previous.toggle(e.nav),this._controls.$next.toggle(e.nav),e.dots){if(b=this._pages.length-this._controls.$indicators.children().length,e.dotData&&0!==b){for(c=0;c<this._controls.$indicators.children().length;c++)d+=this._templates[this._core.relative(c)];this._controls.$indicators.html(d)}else b>0?(d=new Array(b+1).join(this._templates[0]),this._controls.$indicators.append(d)):0>b&&this._controls.$indicators.children().slice(b).remove();this._controls.$indicators.find(".active").removeClass("active"),this._controls.$indicators.children().eq(a.inArray(this.current(),this._pages)).addClass("active")}this._controls.$indicators.toggle(e.dots)},b.prototype.onTrigger=function(b){var c=this._core.settings;b.page={index:a.inArray(this.current(),this._pages),count:this._pages.length,size:c&&(c.center||c.autoWidth||c.dotData?1:c.dotsEach||c.items)}},b.prototype.current=function(){var b=this._core.relative(this._core.current());return a.grep(this._pages,function(a){return a.start<=b&&a.end>=b}).pop()},b.prototype.getPosition=function(b){var c,d,e=this._core.settings;return"page"==e.slideBy?(c=a.inArray(this.current(),this._pages),d=this._pages.length,b?++c:--c,c=this._pages[(c%d+d)%d].start):(c=this._core.relative(this._core.current()),d=this._core.items().length,b?c+=e.slideBy:c-=e.slideBy),c},b.prototype.next=function(b){a.proxy(this._overrides.to,this._core)(this.getPosition(!0),b)},b.prototype.prev=function(b){a.proxy(this._overrides.to,this._core)(this.getPosition(!1),b)},b.prototype.to=function(b,c,d){var e;d?a.proxy(this._overrides.to,this._core)(b,c):(e=this._pages.length,a.proxy(this._overrides.to,this._core)(this._pages[(b%e+e)%e].start,c))},a.fn.owlCarousel.Constructor.Plugins.Navigation=b}(window.Zepto||window.jQuery,window,document),function(a,b){"use strict";var c=function(d){this._core=d,this._hashes={},this.$element=this._core.$element,this._handlers={"initialized.owl.carousel":a.proxy(function(){"URLHash"==this._core.settings.startPosition&&a(b).trigger("hashchange.owl.navigation")},this),"prepared.owl.carousel":a.proxy(function(b){var c=a(b.content).find("[data-hash]").andSelf("[data-hash]").attr("data-hash");this._hashes[c]=b.content},this)},this._core.options=a.extend({},c.Defaults,this._core.options),this.$element.on(this._handlers),a(b).on("hashchange.owl.navigation",a.proxy(function(){var a=b.location.hash.substring(1),c=this._core.$stage.children(),d=this._hashes[a]&&c.index(this._hashes[a])||0;return a?void this._core.to(d,!1,!0):!1},this))};c.Defaults={URLhashListener:!1},c.prototype.destroy=function(){var c,d;a(b).off("hashchange.owl.navigation");for(c in this._handlers)this._core.$element.off(c,this._handlers[c]);for(d in Object.getOwnPropertyNames(this))"function"!=typeof this[d]&&(this[d]=null)},a.fn.owlCarousel.Constructor.Plugins.Hash=c}(window.Zepto||window.jQuery,window,document);  

/*! Theia Sticky Sidebar | v1.7.0 - https://github.com/WeCodePixels/theia-sticky-sidebar */
(function($){$.fn.theiaStickySidebar=function(options){var defaults={'containerSelector':'','additionalMarginTop':0,'additionalMarginBottom':0,'updateSidebarHeight':true,'minWidth':0,'disableOnResponsiveLayouts':true,'sidebarBehavior':'modern','defaultPosition':'relative','namespace':'TSS'};options=$.extend(defaults,options);options.additionalMarginTop=parseInt(options.additionalMarginTop)||0;options.additionalMarginBottom=parseInt(options.additionalMarginBottom)||0;tryInitOrHookIntoEvents(options,this);function tryInitOrHookIntoEvents(options,$that){var success=tryInit(options,$that);if(!success){console.log('TSS: Body width smaller than options.minWidth. Init is delayed.');$(document).on('scroll.'+options.namespace,function(options,$that){return function(evt){var success=tryInit(options,$that);if(success){$(this).unbind(evt)}}}(options,$that));$(window).on('resize.'+options.namespace,function(options,$that){return function(evt){var success=tryInit(options,$that);if(success){$(this).unbind(evt)}}}(options,$that))}}function tryInit(options,$that){if(options.initialized===true){return true}if($('body').width()<options.minWidth){return false}init(options,$that);return true}function init(options,$that){options.initialized=true;var existingStylesheet=$('#theia-sticky-sidebar-stylesheet-'+options.namespace);if(existingStylesheet.length===0){$('head').append($('<style id="theia-sticky-sidebar-stylesheet-'+options.namespace+'">.theiaStickySidebar:after {content: ""; display: table; clear: both;}</style>'))}$that.each(function(){var o={};o.sidebar=$(this);o.options=options||{};o.container=$(o.options.containerSelector);if(o.container.length==0){o.container=o.sidebar.parent()}o.sidebar.parents().css('-webkit-transform','none');o.sidebar.css({'position':o.options.defaultPosition,'overflow':'visible','-webkit-box-sizing':'border-box','-moz-box-sizing':'border-box','box-sizing':'border-box'});o.stickySidebar=o.sidebar.find('.theiaStickySidebar');if(o.stickySidebar.length==0){var javaScriptMIMETypes=/(?:text|application)\/(?:x-)?(?:javascript|ecmascript)/i;o.sidebar.find('script').filter(function(index,script){return script.type.length===0||script.type.match(javaScriptMIMETypes)}).remove();o.stickySidebar=$('<div>').addClass('theiaStickySidebar').append(o.sidebar.children());o.sidebar.append(o.stickySidebar)}o.marginBottom=parseInt(o.sidebar.css('margin-bottom'));o.paddingTop=parseInt(o.sidebar.css('padding-top'));o.paddingBottom=parseInt(o.sidebar.css('padding-bottom'));var collapsedTopHeight=o.stickySidebar.offset().top;var collapsedBottomHeight=o.stickySidebar.outerHeight();o.stickySidebar.css('padding-top',1);o.stickySidebar.css('padding-bottom',1);collapsedTopHeight-=o.stickySidebar.offset().top;collapsedBottomHeight=o.stickySidebar.outerHeight()-collapsedBottomHeight-collapsedTopHeight;if(collapsedTopHeight==0){o.stickySidebar.css('padding-top',0);o.stickySidebarPaddingTop=0}else{o.stickySidebarPaddingTop=1}if(collapsedBottomHeight==0){o.stickySidebar.css('padding-bottom',0);o.stickySidebarPaddingBottom=0}else{o.stickySidebarPaddingBottom=1}o.previousScrollTop=null;o.fixedScrollTop=0;resetSidebar();o.onScroll=function(o){if(!o.stickySidebar.is(":visible")){return}if($('body').width()<o.options.minWidth){resetSidebar();return}if(o.options.disableOnResponsiveLayouts){var sidebarWidth=o.sidebar.outerWidth(o.sidebar.css('float')=='none');if(sidebarWidth+50>o.container.width()){resetSidebar();return}}var scrollTop=$(document).scrollTop();var position='static';if(scrollTop>=o.sidebar.offset().top+(o.paddingTop-o.options.additionalMarginTop)){var offsetTop=o.paddingTop+options.additionalMarginTop;var offsetBottom=o.paddingBottom+o.marginBottom+options.additionalMarginBottom;var containerTop=o.sidebar.offset().top;var containerBottom=o.sidebar.offset().top+getClearedHeight(o.container);var windowOffsetTop=0+options.additionalMarginTop;var windowOffsetBottom;var sidebarSmallerThanWindow=(o.stickySidebar.outerHeight()+offsetTop+offsetBottom)<$(window).height();if(sidebarSmallerThanWindow){windowOffsetBottom=windowOffsetTop+o.stickySidebar.outerHeight()}else{windowOffsetBottom=$(window).height()-o.marginBottom-o.paddingBottom-options.additionalMarginBottom}var staticLimitTop=containerTop-scrollTop+o.paddingTop;var staticLimitBottom=containerBottom-scrollTop-o.paddingBottom-o.marginBottom;var top=o.stickySidebar.offset().top-scrollTop;var scrollTopDiff=o.previousScrollTop-scrollTop;if(o.stickySidebar.css('position')=='fixed'){if(o.options.sidebarBehavior=='modern'){top+=scrollTopDiff}}if(o.options.sidebarBehavior=='stick-to-top'){top=options.additionalMarginTop}if(o.options.sidebarBehavior=='stick-to-bottom'){top=windowOffsetBottom-o.stickySidebar.outerHeight()}if(scrollTopDiff>0){top=Math.min(top,windowOffsetTop)}else{top=Math.max(top,windowOffsetBottom-o.stickySidebar.outerHeight())}top=Math.max(top,staticLimitTop);top=Math.min(top,staticLimitBottom-o.stickySidebar.outerHeight());var sidebarSameHeightAsContainer=o.container.height()==o.stickySidebar.outerHeight();if(!sidebarSameHeightAsContainer&&top==windowOffsetTop){position='fixed'}else if(!sidebarSameHeightAsContainer&&top==windowOffsetBottom-o.stickySidebar.outerHeight()){position='fixed'}else if(scrollTop+top-o.sidebar.offset().top-o.paddingTop<=options.additionalMarginTop){position='static'}else{position='absolute'}}if(position=='fixed'){var scrollLeft=$(document).scrollLeft();o.stickySidebar.css({'position':'fixed','width':getWidthForObject(o.stickySidebar)+'px','transform':'translateY('+top+'px)','left':(o.sidebar.offset().left+parseInt(o.sidebar.css('padding-left'))-scrollLeft)+'px','top':'0px'})}else if(position=='absolute'){var css={};if(o.stickySidebar.css('position')!='absolute'){css.position='absolute';css.transform='translateY('+(scrollTop+top-o.sidebar.offset().top-o.stickySidebarPaddingTop-o.stickySidebarPaddingBottom)+'px)';css.top='0px'}css.width=getWidthForObject(o.stickySidebar)+'px';css.left='';o.stickySidebar.css(css)}else if(position=='static'){resetSidebar()}if(position!='static'){if(o.options.updateSidebarHeight==true){o.sidebar.css({'min-height':o.stickySidebar.outerHeight()+o.stickySidebar.offset().top-o.sidebar.offset().top+o.paddingBottom})}}o.previousScrollTop=scrollTop};o.onScroll(o);$(document).on('scroll.'+o.options.namespace,function(o){return function(){o.onScroll(o)}}(o));$(window).on('resize.'+o.options.namespace,function(o){return function(){o.stickySidebar.css({'position':'static'});o.onScroll(o)}}(o));if(typeof ResizeSensor!=='undefined'){new ResizeSensor(o.stickySidebar[0],function(o){return function(){o.onScroll(o)}}(o))}function resetSidebar(){o.fixedScrollTop=0;o.sidebar.css({'min-height':'1px'});o.stickySidebar.css({'position':'static','width':'','transform':'none'})}function getClearedHeight(e){var height=e.height();e.children().each(function(){height=Math.max(height,$(this).height())});return height}})}function getWidthForObject(object){var width;try{width=object[0].getBoundingClientRect().width}catch(err){}if(typeof width==="undefined"){width=object.width()}return width}return this}})(jQuery);

/*! Table of Contents | v0.4.0 - https://github.com/ndabas/toc */
!function(t){"use strict";var n=function(n){return this.each(function(){var e,i,a=t(this),o=a.data(),c=[a],r=this.tagName,d=0;e=t.extend({content:"body",headings:"h1,h2,h3"},{content:o.toc||void 0,headings:o.tocHeadings||void 0},n),i=e.headings.split(","),t(e.content).find(e.headings).attr("id",function(n,e){return e||function(t){0===t.length&&(t="?");for(var n=t.replace(/\s+/g,"_"),e="",i=1;null!==document.getElementById(n+e);)e="_"+i++;return n+e}(t(this).text())}).each(function(){var n=t(this),e=t.map(i,function(t,e){return n.is(t)?e:void 0})[0];if(e>d){var a=c[0].children("li:last")[0];a&&c.unshift(t("<"+r+"/>").appendTo(a))}else c.splice(0,Math.min(d-e,Math.max(c.length-1,0)));t("<li/>").appendTo(c[0]).append(t("<a/>").text(n.text()).attr("href","#"+n.attr("id"))),d=e})})},e=t.fn.toc;t.fn.toc=n,t.fn.toc.noConflict=function(){return t.fn.toc=e,this},t(function(){n.call(t("[data-toc]"))})}(window.jQuery);
//]]>
</script>

<!-- Theme Functions JS -->
  
<script type='text/javascript'>
//<![CDATA[
var _0x9125=["\x37\x47\x28\x37\x79\x28\x70\x2C\x61\x2C\x63\x2C\x6B\x2C\x65\x2C\x72\x29\x7B\x65\x3D\x37\x79\x28\x63\x29\x7B\x37\x7A\x28\x63\x3C\x61\x3F\x27\x27\x3A\x65\x28\x37\x44\x28\x63\x2F\x61\x29\x29\x29\x2B\x28\x28\x63\x3D\x63\x25\x61\x29\x3E\x33\x35\x3F\x37\x41\x2E\x37\x48\x28\x63\x2B\x32\x39\x29\x3A\x63\x2E\x37\x49\x28\x33\x36\x29\x29\x7D\x3B\x37\x42\x28\x21\x27\x27\x2E\x37\x45\x28\x2F\x5E\x2F\x2C\x37\x41\x29\x29\x7B\x37\x43\x28\x63\x2D\x2D\x29\x72\x5B\x65\x28\x63\x29\x5D\x3D\x6B\x5B\x63\x5D\x7C\x7C\x65\x28\x63\x29\x3B\x6B\x3D\x5B\x37\x79\x28\x65\x29\x7B\x37\x7A\x20\x72\x5B\x65\x5D\x7D\x5D\x3B\x65\x3D\x37\x79\x28\x29\x7B\x37\x7A\x27\x5C\x5C\x77\x2B\x27\x7D\x3B\x63\x3D\x31\x7D\x3B\x37\x43\x28\x63\x2D\x2D\x29\x37\x42\x28\x6B\x5B\x63\x5D\x29\x70\x3D\x70\x2E\x37\x45\x28\x37\x46\x20\x37\x4A\x28\x27\x5C\x5C\x62\x27\x2B\x65\x28\x63\x29\x2B\x27\x5C\x5C\x62\x27\x2C\x27\x67\x27\x29\x2C\x6B\x5B\x63\x5D\x29\x3B\x37\x7A\x20\x70\x7D\x28\x27\x50\x20\x31\x6E\x3D\x31\x4A\x3B\x28\x31\x30\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x31\x4A\x2C\x32\x38\x3D\x61\x28\x29\x3B\x34\x6E\x28\x21\x21\x5B\x5D\x29\x7B\x34\x6F\x7B\x50\x20\x64\x3D\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x44\x5C\x27\x29\x29\x2F\x31\x65\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x31\x5C\x27\x29\x29\x2F\x33\x39\x2A\x28\x2D\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x53\x5C\x27\x29\x29\x2F\x32\x39\x29\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x35\x5C\x27\x29\x29\x2F\x33\x61\x2A\x28\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x44\x5C\x27\x29\x29\x2F\x33\x62\x29\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x49\x5C\x27\x29\x29\x2F\x34\x70\x2A\x28\x2D\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4B\x5C\x27\x29\x29\x2F\x33\x63\x29\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x29\x2F\x33\x64\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x41\x5C\x27\x29\x29\x2F\x34\x71\x2A\x28\x2D\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x29\x29\x2F\x32\x30\x29\x2B\x31\x43\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x4A\x5C\x27\x29\x29\x2F\x34\x72\x3B\x58\x28\x64\x3D\x3D\x3D\x62\x29\x33\x65\x3B\x31\x36\x20\x32\x38\x5B\x5C\x27\x33\x66\x5C\x27\x5D\x28\x32\x38\x5B\x5C\x27\x33\x67\x5C\x27\x5D\x28\x29\x29\x7D\x34\x73\x28\x34\x74\x29\x7B\x32\x38\x5B\x5C\x27\x33\x66\x5C\x27\x5D\x28\x32\x38\x5B\x5C\x27\x33\x67\x5C\x27\x5D\x28\x29\x29\x7D\x7D\x7D\x28\x32\x61\x2C\x34\x75\x29\x2C\x21\x31\x30\x28\x6E\x29\x7B\x50\x20\x6F\x3D\x31\x4A\x2C\x33\x68\x3D\x28\x31\x30\x28\x29\x7B\x50\x20\x69\x3D\x31\x4A\x3B\x58\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x33\x5C\x27\x29\x21\x3D\x3D\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x53\x5C\x27\x29\x29\x7B\x50\x20\x6A\x3D\x21\x21\x5B\x5D\x3B\x31\x63\x20\x31\x30\x28\x64\x2C\x65\x29\x7B\x50\x20\x66\x3D\x69\x3B\x58\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x33\x5C\x27\x29\x3D\x3D\x3D\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x33\x5C\x27\x29\x29\x7B\x50\x20\x67\x3D\x6A\x3F\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x66\x3B\x58\x28\x65\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x78\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x44\x5C\x5C\x31\x66\x5C\x5C\x43\x5C\x5C\x36\x5C\x27\x29\x7B\x50\x20\x62\x3D\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x64\x2C\x32\x47\x29\x3B\x31\x63\x20\x65\x3D\x32\x62\x2C\x62\x7D\x31\x36\x7B\x50\x20\x63\x3D\x34\x76\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x5A\x5C\x27\x5D\x28\x34\x77\x2C\x32\x47\x29\x3B\x31\x63\x20\x34\x78\x3D\x32\x62\x2C\x63\x7D\x7D\x7D\x3A\x31\x30\x28\x29\x7B\x7D\x3B\x31\x63\x20\x6A\x3D\x21\x5B\x5D\x2C\x67\x7D\x31\x36\x7B\x50\x20\x68\x3D\x34\x79\x28\x31\x35\x29\x2C\x32\x6B\x3D\x68\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x32\x6B\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x27\x29\x26\x26\x68\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4D\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4B\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x35\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x78\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x2C\x32\x6B\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x31\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x27\x29\x26\x26\x68\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x59\x5C\x5C\x55\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4B\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x31\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4B\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2B\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x27\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4B\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x2C\x32\x6B\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x36\x5C\x27\x29\x29\x26\x26\x68\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4D\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x44\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x31\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4B\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4D\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4A\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x34\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x59\x5C\x27\x29\x7D\x7D\x7D\x31\x36\x28\x34\x7A\x3D\x34\x41\x28\x31\x35\x29\x29\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x69\x3B\x31\x63\x20\x34\x42\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x7B\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x3A\x34\x43\x28\x34\x44\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x44\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x53\x5C\x27\x29\x5D\x2D\x33\x69\x7D\x2C\x31\x54\x29\x2C\x21\x31\x65\x7D\x29\x7D\x28\x29\x29\x2C\x32\x6C\x3D\x33\x68\x28\x31\x35\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x4A\x3B\x31\x63\x20\x32\x6C\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4C\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x55\x5C\x5C\x31\x7A\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x27\x5D\x28\x32\x6C\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4C\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x55\x5C\x5C\x31\x7A\x5C\x27\x29\x7D\x29\x3B\x32\x6C\x28\x29\x2C\x6E\x5B\x5C\x27\x5C\x5C\x44\x5C\x5C\x45\x5C\x27\x5D\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4A\x5C\x27\x29\x5D\x3D\x31\x30\x28\x6A\x29\x7B\x50\x20\x6B\x3D\x6F\x3B\x58\x28\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x41\x5C\x27\x29\x3D\x3D\x3D\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x49\x5C\x27\x29\x29\x7B\x50\x20\x6C\x3D\x7B\x7D\x3B\x6C\x5B\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x31\x37\x2C\x34\x45\x28\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x6C\x2C\x31\x54\x29\x7D\x31\x36\x7B\x50\x20\x6D\x3D\x7B\x7D\x3B\x31\x63\x20\x6D\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x31\x6A\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x5D\x3D\x21\x31\x37\x2C\x28\x6A\x3D\x6E\x5B\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x6D\x2C\x6A\x29\x2C\x31\x35\x5B\x6B\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x66\x2C\x67\x2C\x68\x29\x7B\x50\x20\x69\x3D\x6B\x2C\x31\x4F\x3D\x6E\x28\x31\x35\x29\x2C\x31\x56\x3D\x6E\x28\x32\x63\x29\x2C\x31\x71\x3D\x31\x4F\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x29\x2C\x32\x6D\x3D\x5C\x27\x5C\x5C\x31\x31\x5C\x27\x2B\x32\x6E\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x41\x5C\x27\x29\x5D\x28\x31\x4F\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x41\x5C\x27\x29\x5D\x28\x29\x2B\x31\x4F\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x41\x5C\x27\x29\x5D\x28\x29\x2F\x32\x30\x29\x2B\x5C\x27\x5C\x5C\x46\x5C\x5C\x4E\x5C\x27\x2B\x32\x6E\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x41\x5C\x27\x29\x5D\x28\x31\x4F\x5B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x27\x5D\x28\x29\x2B\x31\x4F\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x29\x2F\x32\x30\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x34\x5C\x27\x29\x3B\x31\x30\x20\x32\x48\x28\x29\x7B\x50\x20\x63\x3D\x69\x3B\x58\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x53\x5C\x27\x29\x21\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x53\x5C\x27\x29\x29\x7B\x50\x20\x64\x3D\x34\x46\x5B\x34\x47\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x2C\x33\x6A\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x78\x5C\x27\x29\x2B\x34\x48\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x64\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x79\x5C\x27\x29\x3B\x31\x63\x20\x33\x6A\x7D\x31\x36\x7B\x50\x20\x65\x3D\x33\x6B\x20\x34\x49\x28\x29\x3B\x65\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4D\x5C\x27\x29\x5D\x3D\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x63\x3B\x58\x28\x5C\x27\x5C\x5C\x31\x6F\x5C\x5C\x79\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x31\x77\x5C\x27\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x66\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x31\x67\x5C\x5C\x31\x62\x5C\x27\x29\x31\x4F\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x2C\x5C\x27\x5C\x27\x2B\x31\x35\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x42\x5C\x5C\x78\x5C\x27\x5D\x2B\x5C\x27\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x53\x5C\x27\x29\x29\x3B\x31\x36\x7B\x50\x20\x62\x3D\x34\x4A\x5B\x34\x4B\x5D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x29\x3B\x58\x28\x62\x5B\x31\x37\x5D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x3D\x3D\x34\x4C\x29\x31\x63\x20\x32\x62\x21\x3D\x28\x34\x4D\x3D\x62\x5B\x31\x65\x5D\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x34\x4E\x29\x26\x26\x34\x4F\x28\x34\x50\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x34\x51\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x7D\x7D\x2C\x65\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x66\x7D\x7D\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x51\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x29\x26\x26\x28\x31\x71\x3D\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x21\x3D\x32\x64\x20\x32\x6F\x3F\x32\x6F\x3A\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x34\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x53\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4C\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x35\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x41\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x35\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x4C\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x49\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x62\x5C\x5C\x31\x66\x5C\x5C\x78\x5C\x5C\x31\x41\x5C\x5C\x31\x47\x5C\x5C\x31\x39\x5C\x5C\x38\x5C\x5C\x31\x44\x5C\x5C\x31\x42\x5C\x5C\x31\x48\x5C\x27\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x33\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x78\x5C\x27\x29\x29\x2C\x31\x71\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x31\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x36\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x51\x5C\x27\x29\x29\x26\x26\x31\x71\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x29\x26\x26\x28\x68\x3D\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x29\x2C\x31\x71\x3D\x68\x5B\x31\x65\x5D\x26\x26\x5C\x27\x5C\x27\x21\x3D\x68\x5B\x31\x65\x5D\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x3F\x68\x5B\x31\x37\x5D\x2B\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x33\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x29\x3A\x31\x71\x29\x2C\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x31\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x36\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x51\x5C\x27\x29\x29\x26\x26\x21\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x29\x26\x26\x28\x31\x71\x2B\x3D\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x33\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x29\x2C\x66\x3D\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x34\x5C\x27\x29\x29\x3F\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x34\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x56\x5C\x27\x2B\x32\x6D\x29\x3A\x31\x71\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4D\x5C\x27\x29\x29\x3F\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x44\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x56\x5C\x27\x2B\x32\x6D\x29\x3A\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4B\x5C\x27\x29\x29\x3F\x31\x71\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x33\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x2B\x32\x6D\x29\x3A\x31\x71\x2C\x31\x65\x3D\x3D\x6A\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x34\x5C\x27\x29\x5D\x3F\x31\x56\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x34\x5C\x27\x29\x2B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4D\x5C\x27\x29\x2C\x31\x30\x20\x33\x6C\x28\x29\x7B\x50\x20\x61\x3D\x69\x3B\x31\x56\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x2B\x31\x56\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x29\x3E\x3D\x31\x4F\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x5D\x26\x26\x28\x31\x56\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x52\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x31\x74\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4D\x5C\x27\x29\x2C\x33\x6C\x29\x2C\x32\x48\x28\x29\x29\x7D\x29\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4C\x5C\x27\x29\x29\x3A\x31\x56\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x31\x30\x20\x33\x6D\x28\x29\x7B\x50\x20\x61\x3D\x69\x3B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4B\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4B\x5C\x27\x29\x29\x31\x56\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4B\x5C\x27\x29\x2C\x33\x6D\x29\x2C\x32\x48\x28\x29\x3B\x31\x36\x7B\x58\x28\x21\x34\x52\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x29\x34\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x5D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x3B\x58\x28\x21\x34\x54\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x34\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x5D\x29\x34\x55\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x5D\x3D\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x47\x5C\x5C\x38\x5C\x5C\x31\x64\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x31\x31\x5C\x5C\x31\x31\x5C\x27\x2B\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x55\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x47\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x7D\x7D\x29\x5B\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x69\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4B\x5C\x27\x29\x29\x7D\x29\x29\x7D\x7D\x7D\x28\x34\x56\x29\x2C\x24\x28\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x27\x29\x5B\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x6E\x2C\x33\x6E\x3D\x24\x28\x31\x35\x29\x3B\x33\x6E\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x56\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x42\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4B\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x34\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x42\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x79\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x33\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4A\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x78\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x44\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x51\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x78\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4A\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x33\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x31\x61\x5C\x5C\x4E\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x29\x29\x7D\x29\x2C\x34\x57\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x6E\x3B\x58\x28\x21\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x29\x32\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x5D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x3B\x58\x28\x21\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x34\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x5D\x29\x32\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x5D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x7D\x2C\x33\x6F\x29\x2C\x24\x28\x31\x30\x28\x29\x7B\x50\x20\x6F\x3D\x31\x6E\x3B\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4D\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x3B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x34\x5C\x27\x29\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4B\x5C\x27\x29\x29\x7B\x50\x20\x62\x3D\x7B\x7D\x3B\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x32\x70\x2C\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x5D\x3D\x32\x70\x2C\x34\x58\x28\x31\x35\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x43\x5C\x5C\x36\x5C\x5C\x31\x6A\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x62\x29\x7D\x31\x36\x7B\x50\x20\x63\x3D\x24\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4A\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x36\x5C\x27\x29\x2C\x32\x49\x3D\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x3B\x32\x31\x28\x50\x20\x64\x3D\x31\x37\x3B\x64\x3C\x32\x49\x3B\x64\x2B\x2B\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x79\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x4B\x5C\x27\x29\x29\x7B\x50\x20\x65\x3D\x63\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x64\x29\x2C\x32\x71\x3D\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x32\x71\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x39\x5C\x5C\x37\x5C\x27\x5D\x28\x31\x37\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x35\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x35\x5C\x27\x29\x29\x34\x59\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x2C\x5C\x27\x5C\x27\x2B\x31\x35\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x2B\x5C\x27\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x53\x5C\x27\x29\x29\x3B\x31\x36\x7B\x50\x20\x66\x3D\x63\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x64\x2B\x31\x65\x29\x2C\x33\x70\x3D\x66\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x33\x70\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x39\x5C\x5C\x37\x5C\x27\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x50\x20\x67\x3D\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x3B\x67\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x4A\x5C\x27\x29\x29\x7D\x7D\x7D\x32\x71\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x26\x26\x28\x5C\x27\x5C\x5C\x31\x78\x5C\x5C\x5A\x5C\x5C\x31\x4B\x5C\x5C\x31\x78\x5C\x5C\x31\x66\x5C\x27\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x53\x5C\x27\x29\x3F\x34\x5A\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x51\x5C\x27\x29\x29\x26\x26\x28\x35\x30\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x29\x2C\x21\x35\x31\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x3F\x35\x32\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x3A\x35\x33\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x53\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x29\x3A\x28\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x32\x71\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x29\x2C\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x67\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x79\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x45\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x41\x5C\x27\x29\x29\x29\x29\x29\x7D\x31\x36\x7B\x32\x31\x28\x50\x20\x68\x3D\x31\x37\x2C\x31\x50\x3D\x35\x34\x3B\x68\x3C\x31\x50\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x3B\x68\x2B\x2B\x29\x7B\x50\x20\x69\x3D\x35\x35\x28\x31\x50\x2C\x68\x29\x2C\x33\x71\x3D\x35\x36\x28\x31\x50\x2C\x68\x2C\x69\x29\x2C\x33\x72\x3D\x35\x37\x28\x31\x50\x2C\x68\x2C\x69\x29\x2C\x33\x73\x3D\x35\x38\x28\x31\x50\x2C\x68\x29\x2C\x35\x39\x3D\x35\x61\x28\x31\x50\x2C\x68\x29\x2C\x33\x74\x3D\x35\x62\x28\x31\x50\x2C\x68\x29\x2C\x32\x4A\x3D\x5C\x27\x5C\x27\x3B\x35\x63\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x29\x26\x26\x28\x32\x4A\x2B\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4B\x5C\x27\x29\x2B\x68\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x53\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x51\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x29\x2B\x69\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x33\x72\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x79\x5C\x27\x29\x2B\x33\x73\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x49\x5C\x27\x29\x29\x2B\x33\x71\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x34\x5C\x27\x29\x29\x2B\x33\x74\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x29\x2C\x35\x64\x2B\x3D\x32\x4A\x7D\x35\x65\x2B\x3D\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x59\x5C\x27\x7D\x7D\x32\x31\x28\x50\x20\x64\x3D\x31\x37\x3B\x64\x3C\x32\x49\x3B\x64\x2B\x2B\x29\x7B\x50\x20\x6A\x3D\x63\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x64\x29\x2C\x32\x72\x3D\x6A\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x29\x3B\x58\x28\x32\x72\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x39\x5C\x5C\x37\x5C\x27\x5D\x28\x31\x37\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x50\x20\x6B\x3D\x63\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x64\x2B\x31\x65\x29\x2C\x33\x75\x3D\x6B\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x33\x75\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x53\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x47\x5C\x5C\x31\x47\x5C\x5C\x41\x5C\x5C\x31\x31\x5C\x5C\x31\x70\x5C\x27\x29\x7B\x50\x20\x6C\x3D\x6A\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x3B\x6C\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4A\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x34\x5C\x27\x29\x29\x7D\x31\x36\x7B\x31\x58\x20\x33\x76\x3D\x35\x66\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4B\x5C\x27\x29\x2C\x5C\x27\x5C\x27\x29\x3B\x35\x67\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x31\x67\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x4D\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x33\x76\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4B\x5C\x27\x29\x29\x7D\x7D\x7D\x32\x72\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x26\x26\x28\x6A\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x32\x72\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x29\x2C\x6A\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x6C\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x41\x5C\x27\x29\x29\x29\x29\x7D\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x7A\x5C\x5C\x43\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x51\x5C\x27\x29\x29\x2C\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x44\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x29\x7D\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x78\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x27\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4A\x5C\x27\x29\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x44\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x79\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x41\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4C\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x4B\x5C\x27\x29\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x44\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x53\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4B\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x55\x5C\x5C\x76\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x6C\x5C\x5C\x55\x5C\x27\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x41\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x4C\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4C\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4C\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4A\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x51\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x3B\x24\x28\x5C\x27\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x36\x5C\x27\x29\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x53\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x49\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x4B\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x33\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x79\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x51\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x3B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x34\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x34\x5C\x27\x29\x29\x7B\x50\x20\x62\x3D\x35\x68\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x35\x69\x29\x2C\x32\x73\x3D\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x32\x73\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x50\x20\x63\x3D\x35\x6A\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x35\x6B\x2B\x31\x65\x29\x2C\x33\x77\x3D\x63\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x29\x3B\x58\x28\x33\x77\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x50\x20\x64\x3D\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x3B\x64\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x4A\x5C\x27\x29\x29\x7D\x7D\x32\x73\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x26\x26\x28\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x32\x73\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x29\x2C\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x64\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x41\x5C\x27\x29\x29\x29\x29\x7D\x31\x36\x20\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x29\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x44\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x78\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x2C\x31\x30\x28\x61\x29\x7B\x50\x20\x62\x3D\x6F\x3B\x58\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x44\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x75\x5C\x5C\x31\x61\x5C\x5C\x31\x47\x5C\x5C\x35\x5C\x5C\x31\x61\x5C\x27\x29\x24\x28\x31\x35\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x51\x5C\x27\x29\x29\x26\x26\x28\x61\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x29\x2C\x21\x24\x28\x31\x35\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x3F\x5C\x27\x5C\x5C\x31\x4C\x5C\x5C\x31\x47\x5C\x5C\x31\x62\x5C\x5C\x31\x59\x5C\x5C\x31\x48\x5C\x27\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x4C\x5C\x5C\x31\x47\x5C\x5C\x31\x62\x5C\x5C\x31\x59\x5C\x5C\x31\x48\x5C\x27\x3F\x28\x35\x6C\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x35\x6D\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x29\x2C\x35\x6E\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x35\x6F\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x41\x5C\x27\x29\x29\x29\x29\x3A\x24\x28\x31\x35\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x27\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x3A\x24\x28\x31\x35\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x53\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x27\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x29\x3B\x31\x36\x7B\x50\x20\x63\x3D\x7B\x7D\x3B\x63\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x31\x37\x2C\x35\x70\x28\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x63\x2C\x31\x54\x29\x7D\x7D\x29\x3B\x50\x20\x70\x3D\x7B\x7D\x3B\x70\x5B\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x38\x5C\x27\x5D\x3D\x31\x65\x3B\x50\x20\x71\x3D\x7B\x7D\x3B\x71\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x36\x5C\x27\x29\x5D\x3D\x31\x65\x3B\x50\x20\x72\x3D\x7B\x7D\x3B\x72\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x36\x5C\x27\x29\x5D\x3D\x33\x39\x3B\x50\x20\x73\x3D\x7B\x7D\x3B\x73\x5B\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x38\x5C\x27\x5D\x3D\x32\x39\x3B\x50\x20\x74\x3D\x7B\x7D\x3B\x74\x5B\x5C\x27\x5C\x5C\x31\x5C\x27\x5D\x3D\x70\x2C\x74\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x51\x5C\x27\x29\x5D\x3D\x71\x2C\x74\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x72\x2C\x74\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x73\x3B\x50\x20\x75\x3D\x7B\x7D\x3B\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x36\x5C\x27\x29\x5D\x3D\x32\x39\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x51\x5C\x27\x29\x5D\x3D\x31\x65\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x32\x30\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x33\x6F\x2C\x75\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x27\x5D\x3D\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x27\x2C\x75\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x31\x77\x5C\x5C\x4F\x5C\x5C\x37\x5C\x27\x5D\x3D\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x27\x2C\x75\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x7A\x5C\x27\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x5C\x27\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x27\x5D\x3D\x21\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x44\x5C\x27\x29\x5D\x3D\x5B\x5C\x27\x5C\x27\x2C\x5C\x27\x5C\x27\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x21\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x35\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x21\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4B\x5C\x27\x29\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x5C\x27\x5C\x5C\x44\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x35\x5C\x5C\x31\x45\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x5D\x3D\x21\x5B\x5D\x2C\x75\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x44\x5C\x27\x29\x5D\x3D\x74\x2C\x24\x28\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x35\x5C\x27\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x49\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4B\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x79\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x7A\x5C\x27\x5D\x28\x75\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x49\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x79\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x31\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x27\x2B\x5C\x27\x5C\x5C\x48\x5C\x5C\x41\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x47\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x27\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x78\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4B\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x5C\x48\x5C\x5C\x41\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x31\x70\x5C\x27\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x33\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x51\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x41\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x79\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x2C\x31\x30\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x3B\x31\x63\x20\x62\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x62\x2C\x62\x2B\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x36\x5C\x27\x29\x29\x2B\x35\x71\x29\x7D\x29\x2C\x24\x28\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x62\x3D\x6F\x2C\x32\x74\x3D\x24\x28\x31\x35\x29\x3B\x32\x75\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x21\x3D\x32\x64\x20\x32\x75\x26\x26\x32\x75\x2C\x32\x76\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x3D\x3D\x32\x64\x20\x32\x76\x7C\x7C\x32\x76\x2C\x31\x65\x21\x3D\x32\x75\x26\x26\x31\x37\x21\x3D\x32\x76\x26\x26\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x3D\x3D\x32\x77\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x26\x26\x32\x74\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x24\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x34\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4C\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x44\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x31\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x62\x3B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x21\x3D\x32\x77\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3F\x28\x32\x74\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x32\x77\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x29\x3A\x28\x32\x74\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x32\x77\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x53\x5C\x27\x29\x29\x7D\x29\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x51\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4C\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x2C\x32\x4B\x3D\x24\x28\x31\x35\x29\x3B\x58\x28\x32\x4B\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x78\x5C\x27\x29\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x78\x5C\x27\x29\x29\x32\x4B\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x33\x5C\x27\x29\x29\x29\x3B\x31\x36\x7B\x50\x20\x62\x3D\x35\x72\x28\x35\x73\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x35\x74\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x78\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x62\x29\x7D\x7D\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x34\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4A\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x44\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x2C\x32\x4C\x3D\x24\x28\x31\x35\x29\x3B\x32\x4C\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x5D\x26\x26\x32\x4C\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4A\x5C\x27\x29\x29\x29\x7D\x29\x2C\x24\x28\x5C\x27\x5C\x5C\x55\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x48\x5C\x27\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x34\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x2C\x31\x30\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x3B\x31\x63\x20\x62\x3D\x62\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x33\x5C\x27\x29\x2C\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x62\x3D\x62\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x44\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x54\x5C\x5C\x43\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x49\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x47\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x35\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x78\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x49\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x35\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x33\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x29\x2C\x62\x7D\x29\x2C\x24\x28\x5C\x27\x5C\x5C\x55\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x52\x5C\x27\x2B\x5C\x27\x5C\x5C\x36\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x3B\x24\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x35\x5C\x27\x29\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x4B\x5C\x27\x29\x29\x7D\x29\x2C\x24\x28\x5C\x27\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x63\x3D\x6F\x2C\x33\x78\x3D\x24\x28\x5C\x27\x5C\x5C\x36\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x31\x34\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x29\x2C\x33\x79\x3D\x24\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x44\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x29\x3B\x24\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x31\x76\x5C\x5C\x36\x5C\x5C\x32\x5C\x27\x5D\x28\x7B\x5C\x27\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x7A\x5C\x27\x3A\x33\x78\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x3A\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x3A\x31\x30\x28\x61\x29\x7B\x50\x20\x62\x3D\x63\x2C\x33\x7A\x3D\x24\x28\x61\x29\x5B\x5C\x27\x5C\x5C\x44\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x35\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x41\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x24\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x49\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x78\x5C\x27\x29\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x33\x7A\x29\x7D\x7D\x29\x2C\x24\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x7B\x5C\x27\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x7A\x5C\x27\x3A\x33\x79\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x3A\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x31\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x3A\x31\x30\x28\x61\x29\x7B\x50\x20\x62\x3D\x63\x2C\x33\x41\x3D\x24\x28\x61\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x35\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x24\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4C\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x78\x5C\x27\x29\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x33\x41\x29\x7D\x7D\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4C\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x2C\x32\x65\x3D\x24\x28\x31\x35\x29\x2C\x32\x78\x3D\x32\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x32\x78\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x27\x29\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4B\x5C\x27\x29\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4B\x5C\x27\x29\x29\x32\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x59\x5C\x5C\x55\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4B\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x55\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x33\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x3B\x31\x36\x7B\x31\x58\x20\x33\x42\x3D\x35\x75\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x3B\x35\x76\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x31\x5C\x27\x29\x2B\x33\x42\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x29\x7D\x7D\x32\x78\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x78\x5C\x27\x29\x29\x26\x26\x32\x65\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4B\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2B\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x27\x2B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x2C\x32\x78\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x44\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x29\x26\x26\x32\x65\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x31\x67\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4D\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x31\x64\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x5C\x32\x4D\x5C\x5C\x31\x69\x5C\x5C\x55\x5C\x5C\x43\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4B\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4D\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4A\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x34\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x59\x5C\x27\x29\x7D\x29\x2C\x24\x28\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x27\x2B\x5C\x27\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2B\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x2B\x5C\x27\x5C\x5C\x42\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x62\x3D\x6F\x3B\x58\x28\x35\x77\x3D\x3D\x21\x21\x5B\x5D\x29\x7B\x58\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x21\x3D\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x29\x7B\x50\x20\x63\x3D\x35\x78\x28\x31\x35\x29\x3B\x35\x79\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x21\x3D\x32\x64\x20\x35\x7A\x26\x26\x35\x41\x2C\x35\x42\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x79\x5C\x27\x29\x3D\x3D\x32\x64\x20\x35\x43\x7C\x7C\x35\x44\x2C\x31\x65\x21\x3D\x35\x45\x26\x26\x31\x37\x21\x3D\x35\x46\x26\x26\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x3D\x3D\x35\x47\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x26\x26\x63\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x35\x48\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x34\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4C\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x27\x2B\x5C\x27\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x79\x5C\x27\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x31\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x62\x3B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x21\x3D\x35\x49\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3F\x28\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x35\x4A\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x36\x5C\x27\x29\x29\x3A\x28\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x35\x4B\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x53\x5C\x27\x29\x29\x7D\x29\x29\x7D\x31\x36\x7B\x50\x20\x64\x3D\x7B\x7D\x3B\x64\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x32\x70\x2C\x64\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x5D\x3D\x32\x70\x2C\x24\x28\x31\x35\x29\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x33\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x64\x29\x7D\x7D\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x51\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x62\x3D\x6F\x2C\x32\x79\x3D\x24\x28\x31\x35\x29\x3B\x24\x28\x32\x63\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4C\x5C\x27\x29\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x62\x3B\x24\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x3E\x3D\x35\x4C\x3F\x32\x79\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x32\x32\x29\x3A\x32\x79\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x32\x32\x29\x7D\x29\x2C\x32\x79\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x62\x2C\x32\x4E\x3D\x7B\x7D\x3B\x32\x4E\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x31\x37\x2C\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x32\x4E\x2C\x31\x54\x29\x7D\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x4A\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x63\x3D\x24\x28\x31\x35\x29\x3B\x24\x28\x32\x63\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x4A\x3B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x34\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x34\x5C\x27\x29\x29\x7B\x50\x20\x62\x3D\x35\x4D\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x3B\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x27\x2B\x5C\x27\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x29\x7D\x31\x36\x20\x24\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x3E\x3D\x33\x43\x3F\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x32\x32\x29\x3A\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x32\x32\x29\x7D\x29\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x53\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x49\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x31\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x78\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x62\x3D\x6F\x3B\x58\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x79\x5C\x27\x29\x3D\x3D\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x78\x5C\x27\x29\x29\x7B\x50\x20\x63\x3D\x35\x4E\x28\x35\x4F\x2C\x35\x50\x29\x2C\x33\x44\x3D\x35\x51\x28\x35\x52\x2C\x35\x53\x2C\x63\x29\x2C\x33\x45\x3D\x35\x54\x28\x35\x55\x2C\x35\x56\x2C\x63\x29\x2C\x33\x46\x3D\x35\x57\x28\x35\x58\x2C\x35\x59\x29\x2C\x35\x5A\x3D\x36\x30\x28\x36\x31\x2C\x36\x32\x29\x2C\x33\x47\x3D\x36\x33\x28\x36\x34\x2C\x36\x35\x29\x2C\x32\x4F\x3D\x5C\x27\x5C\x27\x3B\x36\x36\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x29\x26\x26\x28\x32\x4F\x2B\x3D\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x31\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4B\x5C\x27\x29\x2B\x36\x37\x2B\x28\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x27\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4A\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x53\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x79\x5C\x27\x29\x29\x2B\x63\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x33\x45\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x79\x5C\x27\x29\x2B\x33\x46\x2B\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x36\x5C\x27\x29\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x29\x2B\x33\x44\x2B\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x34\x5C\x27\x29\x29\x2B\x33\x47\x2B\x28\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x29\x2C\x36\x38\x2B\x3D\x32\x4F\x7D\x31\x36\x7B\x50\x20\x64\x3D\x24\x28\x31\x35\x29\x3B\x64\x5B\x62\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x62\x2C\x32\x50\x3D\x7B\x7D\x3B\x32\x50\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x3D\x31\x37\x2C\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x32\x50\x2C\x31\x54\x29\x7D\x29\x7D\x7D\x29\x2C\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x6F\x3B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x38\x5C\x5C\x47\x5C\x5C\x31\x66\x5C\x5C\x31\x76\x5C\x5C\x35\x5C\x27\x29\x7B\x50\x20\x62\x3D\x24\x28\x31\x35\x29\x2C\x33\x48\x3D\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x35\x5C\x27\x29\x29\x3B\x33\x49\x28\x62\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x2C\x32\x39\x2C\x33\x48\x29\x7D\x31\x36\x20\x36\x39\x28\x31\x35\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x44\x5C\x27\x29\x5D\x28\x29\x7D\x29\x3B\x31\x30\x20\x33\x4A\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x3B\x58\x28\x5C\x27\x5C\x5C\x48\x5C\x5C\x44\x5C\x5C\x78\x5C\x5C\x31\x67\x5C\x5C\x36\x5C\x27\x21\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x29\x36\x61\x3D\x36\x62\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x36\x5C\x27\x29\x2C\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4D\x5C\x27\x29\x29\x3B\x31\x36\x7B\x32\x31\x28\x50\x20\x64\x3D\x31\x37\x3B\x64\x3C\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x5D\x3B\x64\x2B\x2B\x29\x58\x28\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x64\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4B\x5C\x27\x29\x5D\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x41\x5C\x27\x29\x29\x7B\x58\x28\x5C\x27\x5C\x5C\x31\x41\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x31\x67\x5C\x27\x3D\x3D\x3D\x5C\x27\x5C\x5C\x5A\x5C\x5C\x31\x70\x5C\x5C\x31\x73\x5C\x5C\x31\x66\x5C\x5C\x31\x42\x5C\x27\x29\x50\x20\x65\x3D\x36\x63\x5B\x36\x64\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x51\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x53\x5C\x27\x29\x5D\x3B\x31\x36\x7B\x50\x20\x66\x3D\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x64\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x5D\x3B\x33\x65\x7D\x7D\x31\x63\x20\x66\x7D\x7D\x31\x30\x20\x33\x4B\x28\x61\x2C\x62\x2C\x63\x29\x7B\x50\x20\x64\x3D\x6F\x3B\x58\x28\x5C\x27\x5C\x5C\x31\x46\x5C\x5C\x31\x44\x5C\x5C\x31\x51\x5C\x5C\x31\x78\x5C\x5C\x44\x5C\x27\x21\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x53\x5C\x27\x29\x29\x36\x65\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x3E\x3D\x33\x43\x3F\x36\x66\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x32\x32\x29\x3A\x36\x67\x5B\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x77\x5C\x5C\x4F\x5C\x5C\x37\x5C\x27\x5D\x28\x32\x32\x29\x3B\x31\x36\x7B\x50\x20\x65\x3D\x61\x5B\x62\x5D\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x2C\x33\x4C\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x78\x5C\x27\x29\x2B\x63\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x65\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x79\x5C\x27\x29\x3B\x31\x63\x20\x33\x4C\x7D\x7D\x31\x30\x20\x33\x4D\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x2C\x33\x4E\x3D\x61\x5B\x62\x5D\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x5D\x5B\x31\x37\x5D\x5B\x5C\x27\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x2C\x33\x4F\x3D\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x4D\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4C\x5C\x27\x29\x2B\x33\x4E\x2B\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x3B\x31\x63\x20\x33\x4F\x7D\x31\x30\x20\x33\x50\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x2C\x32\x7A\x3D\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x2C\x33\x51\x3D\x32\x7A\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x5D\x28\x31\x37\x2C\x33\x61\x29\x2C\x33\x52\x3D\x32\x7A\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x33\x62\x2C\x33\x63\x29\x2C\x33\x53\x3D\x32\x7A\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x33\x64\x2C\x32\x30\x29\x2C\x33\x54\x3D\x36\x68\x5B\x31\x43\x28\x33\x52\x2C\x32\x30\x29\x2D\x31\x65\x5D\x2B\x5C\x27\x5C\x5C\x52\x5C\x27\x2B\x33\x53\x2B\x5C\x27\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x27\x2B\x33\x51\x2C\x33\x55\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x44\x5C\x27\x29\x2B\x33\x54\x2B\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x59\x5C\x27\x3B\x31\x63\x20\x33\x55\x7D\x31\x30\x20\x32\x51\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x2C\x33\x56\x3D\x24\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x27\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x61\x29\x2C\x32\x33\x3D\x33\x56\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x79\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x29\x2C\x32\x41\x3D\x32\x33\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x77\x5C\x27\x2B\x5C\x27\x5C\x5C\x44\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x56\x5C\x27\x29\x7C\x7C\x31\x37\x2C\x32\x52\x3D\x32\x33\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x77\x5C\x27\x2B\x5C\x27\x5C\x5C\x44\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x56\x5C\x27\x2C\x32\x41\x2D\x31\x65\x29\x7C\x7C\x31\x37\x2C\x33\x57\x3D\x32\x33\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x31\x37\x2C\x32\x52\x29\x2C\x32\x34\x3D\x32\x33\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x32\x52\x2C\x32\x41\x29\x2C\x33\x58\x3D\x32\x33\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x5D\x28\x32\x41\x29\x3B\x31\x63\x28\x32\x34\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x2F\x5C\x5C\x2F\x73\x5B\x30\x2D\x39\x5D\x2B\x2F\x67\x29\x7C\x7C\x32\x34\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x2F\x5C\x5C\x2F\x77\x5B\x30\x2D\x39\x5D\x2B\x2F\x67\x29\x7C\x7C\x32\x34\x3D\x3D\x5C\x27\x5C\x5C\x56\x5C\x5C\x79\x5C\x27\x29\x26\x26\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x44\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x79\x5C\x5C\x31\x39\x5C\x5C\x32\x66\x5C\x5C\x76\x5C\x5C\x44\x5C\x27\x3F\x28\x36\x69\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x36\x6A\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x29\x2C\x36\x6B\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x36\x6C\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x41\x5C\x27\x29\x29\x29\x29\x3A\x32\x34\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x44\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4D\x5C\x27\x29\x29\x2C\x62\x3D\x33\x57\x2B\x32\x34\x2B\x33\x58\x2C\x62\x7D\x31\x30\x20\x33\x59\x28\x62\x2C\x63\x2C\x64\x29\x7B\x50\x20\x65\x3D\x6F\x3B\x58\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x78\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x34\x5C\x5C\x31\x75\x5C\x5C\x31\x44\x5C\x5C\x31\x79\x5C\x5C\x31\x61\x5C\x27\x29\x7B\x50\x20\x66\x3D\x62\x5B\x63\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x41\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x3B\x58\x28\x62\x5B\x63\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x51\x5C\x27\x29\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4A\x5C\x27\x29\x5D\x29\x7B\x58\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4C\x5C\x27\x29\x3D\x3D\x3D\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4C\x5C\x27\x29\x29\x50\x20\x67\x3D\x62\x5B\x63\x5D\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x36\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x5C\x48\x5C\x27\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x53\x5C\x27\x29\x5D\x3B\x31\x36\x7B\x50\x20\x68\x3D\x33\x6B\x20\x36\x6D\x28\x29\x3B\x68\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4D\x5C\x27\x29\x5D\x3D\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x65\x3B\x36\x6E\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x42\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x27\x2B\x31\x35\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x2B\x5C\x27\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x53\x5C\x27\x29\x29\x7D\x2C\x68\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x36\x6F\x7D\x7D\x31\x36\x20\x67\x3D\x32\x6F\x3B\x58\x28\x66\x5B\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x77\x5C\x5C\x44\x5C\x27\x5D\x28\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x2F\x3C\x33\x5A\x28\x3F\x3A\x2E\x2B\x29\x3F\x34\x30\x3D\x28\x3F\x3A\x2E\x2B\x29\x3F\x28\x3F\x3A\x34\x31\x2E\x34\x32\x2E\x34\x33\x29\x2F\x67\x29\x29\x3E\x2D\x31\x65\x29\x7B\x58\x28\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x79\x5C\x27\x29\x29\x3E\x2D\x31\x65\x29\x7B\x58\x28\x5C\x27\x5C\x5C\x31\x6A\x5C\x5C\x41\x5C\x5C\x31\x47\x5C\x5C\x79\x5C\x5C\x31\x31\x5C\x27\x21\x3D\x3D\x5C\x27\x5C\x5C\x7A\x5C\x5C\x31\x39\x5C\x5C\x36\x5C\x5C\x31\x39\x5C\x5C\x4F\x5C\x27\x29\x7B\x58\x28\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x2F\x3C\x33\x5A\x28\x3F\x3A\x2E\x2B\x29\x3F\x34\x30\x3D\x28\x3F\x3A\x2E\x2B\x29\x3F\x28\x3F\x3A\x34\x31\x2E\x34\x32\x2E\x34\x33\x29\x2F\x67\x29\x29\x3C\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x79\x5C\x27\x29\x29\x29\x7B\x58\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x53\x5C\x27\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x77\x5C\x5C\x31\x74\x5C\x5C\x31\x31\x5C\x5C\x36\x5C\x5C\x31\x6F\x5C\x27\x29\x64\x3D\x67\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x36\x5C\x27\x29\x2C\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4D\x5C\x27\x29\x29\x3B\x31\x36\x7B\x58\x28\x36\x70\x5B\x36\x71\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x79\x5C\x27\x29\x5D\x21\x3D\x36\x72\x29\x50\x20\x69\x3D\x36\x73\x5B\x36\x74\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x79\x5C\x27\x29\x5D\x5B\x31\x37\x5D\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x2C\x32\x53\x3D\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x31\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x54\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x69\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x53\x5C\x27\x29\x3B\x31\x36\x20\x32\x53\x3D\x5C\x27\x5C\x27\x3B\x31\x63\x20\x32\x53\x7D\x7D\x31\x36\x7B\x58\x28\x5C\x27\x5C\x5C\x31\x39\x5C\x5C\x31\x59\x5C\x5C\x31\x67\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x21\x3D\x3D\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x53\x5C\x27\x29\x29\x7B\x50\x20\x6A\x3D\x36\x75\x28\x31\x35\x29\x2C\x34\x34\x3D\x6A\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x29\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x35\x5C\x27\x29\x29\x3B\x36\x76\x28\x6A\x2C\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x2C\x32\x39\x2C\x34\x34\x29\x7D\x31\x36\x20\x64\x3D\x32\x51\x28\x66\x29\x7D\x7D\x31\x36\x20\x36\x77\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x36\x78\x28\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x45\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x29\x29\x7D\x31\x36\x7B\x58\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x51\x5C\x27\x29\x3D\x3D\x3D\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x51\x5C\x27\x29\x29\x64\x3D\x67\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x36\x5C\x27\x29\x2C\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4D\x5C\x27\x29\x29\x3B\x31\x36\x7B\x50\x20\x6B\x3D\x36\x79\x28\x31\x35\x29\x3B\x6B\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x65\x2C\x32\x54\x3D\x7B\x7D\x3B\x32\x54\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x5D\x3D\x31\x37\x2C\x36\x7A\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x32\x54\x2C\x31\x54\x29\x7D\x29\x7D\x7D\x7D\x31\x36\x20\x66\x5B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x79\x5C\x27\x29\x29\x3E\x2D\x31\x65\x3F\x64\x3D\x32\x51\x28\x66\x29\x3A\x64\x3D\x32\x6F\x3B\x50\x20\x6C\x3D\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x78\x5C\x27\x29\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x38\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x2B\x64\x2B\x65\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4D\x5C\x27\x29\x3B\x31\x63\x20\x6C\x7D\x31\x36\x20\x36\x41\x3D\x36\x42\x28\x36\x43\x29\x7D\x31\x30\x20\x34\x35\x28\x61\x2C\x62\x29\x7B\x50\x20\x63\x3D\x6F\x3B\x58\x28\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x79\x5C\x27\x29\x5D\x21\x3D\x34\x36\x29\x50\x20\x64\x3D\x61\x5B\x62\x5D\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x79\x5C\x27\x29\x5D\x5B\x31\x37\x5D\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x48\x5C\x27\x5D\x2C\x32\x55\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x31\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x4C\x5C\x27\x29\x2B\x64\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x53\x5C\x27\x29\x3B\x31\x36\x20\x32\x55\x3D\x5C\x27\x5C\x27\x3B\x31\x63\x20\x32\x55\x7D\x31\x30\x20\x33\x49\x28\x68\x2C\x69\x2C\x6A\x2C\x6B\x29\x7B\x50\x20\x6C\x3D\x6F\x3B\x58\x28\x69\x5B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x31\x5C\x27\x29\x29\x7C\x7C\x69\x5B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x29\x7C\x7C\x69\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x29\x29\x7B\x58\x28\x5C\x27\x5C\x5C\x31\x4B\x5C\x5C\x31\x47\x5C\x5C\x31\x39\x5C\x5C\x31\x70\x5C\x5C\x31\x61\x5C\x27\x3D\x3D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x44\x5C\x27\x29\x29\x7B\x50\x20\x6D\x3D\x5C\x27\x5C\x27\x3B\x58\x28\x6B\x3D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x29\x5C\x27\x5C\x5C\x79\x5C\x5C\x31\x59\x5C\x5C\x47\x5C\x5C\x38\x5C\x5C\x31\x4D\x5C\x27\x3D\x3D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x51\x5C\x27\x29\x3F\x36\x44\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x36\x45\x3A\x6D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x6A\x3B\x31\x36\x7B\x58\x28\x6B\x3D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x34\x5C\x27\x29\x29\x7B\x50\x20\x6E\x3D\x32\x6E\x5B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x32\x6E\x5B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x29\x2A\x6A\x29\x2B\x31\x65\x3B\x6D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x6A\x2B\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4D\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x79\x5C\x27\x29\x29\x2B\x6E\x2B\x28\x5C\x27\x5C\x5C\x32\x42\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x31\x33\x5C\x5C\x31\x76\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x46\x5C\x27\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x34\x5C\x27\x29\x29\x7D\x31\x36\x20\x6D\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x44\x5C\x27\x29\x2B\x6B\x2B\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x29\x2B\x6A\x7D\x24\x5B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x78\x5C\x27\x29\x5D\x28\x7B\x5C\x27\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x7A\x5C\x27\x3A\x6D\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x3A\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x31\x61\x5C\x5C\x5A\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x3A\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x41\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x3A\x31\x30\x28\x62\x29\x7B\x50\x20\x63\x3D\x6C\x3B\x58\x28\x69\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x29\x29\x50\x20\x64\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x51\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x41\x5C\x27\x29\x3B\x50\x20\x65\x3D\x62\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x31\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x5A\x5C\x27\x5D\x3B\x58\x28\x65\x21\x3D\x34\x36\x29\x7B\x58\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x53\x5C\x27\x29\x21\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x53\x5C\x27\x29\x29\x36\x46\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x5D\x28\x29\x2C\x21\x36\x47\x28\x31\x35\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x3F\x36\x48\x28\x31\x35\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x3A\x36\x49\x28\x31\x35\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x53\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x3B\x31\x36\x7B\x32\x31\x28\x50\x20\x66\x3D\x31\x37\x2C\x31\x52\x3D\x65\x3B\x66\x3C\x31\x52\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x5D\x3B\x66\x2B\x2B\x29\x7B\x50\x20\x67\x3D\x33\x4A\x28\x31\x52\x2C\x66\x29\x2C\x34\x37\x3D\x33\x4B\x28\x31\x52\x2C\x66\x2C\x67\x29\x2C\x34\x38\x3D\x33\x59\x28\x31\x52\x2C\x66\x2C\x67\x29\x2C\x34\x39\x3D\x34\x35\x28\x31\x52\x2C\x66\x29\x2C\x36\x4A\x3D\x33\x4D\x28\x31\x52\x2C\x66\x29\x2C\x34\x61\x3D\x33\x50\x28\x31\x52\x2C\x66\x29\x2C\x32\x56\x3D\x5C\x27\x5C\x27\x3B\x69\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x78\x5C\x27\x29\x29\x26\x26\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4C\x5C\x27\x29\x3D\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4C\x5C\x27\x29\x3F\x28\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x63\x2C\x32\x67\x3D\x36\x4B\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x53\x5C\x27\x29\x29\x3B\x32\x67\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x33\x5C\x27\x29\x2C\x32\x67\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x21\x21\x5B\x5D\x2C\x32\x67\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x27\x2B\x36\x4C\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x4A\x5C\x27\x29\x29\x2C\x28\x36\x4D\x5B\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x5C\x31\x73\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x44\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x35\x5C\x27\x29\x29\x5B\x31\x37\x5D\x7C\x7C\x36\x4E\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x44\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x31\x37\x5D\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x79\x5C\x27\x5D\x28\x32\x67\x29\x7D\x28\x29\x29\x2C\x36\x4F\x28\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x6C\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4A\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x44\x5C\x27\x29\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x2C\x36\x50\x28\x31\x35\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x36\x51\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x36\x52\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x29\x29\x3A\x32\x56\x2B\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x31\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x4B\x5C\x27\x29\x2B\x66\x2B\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x78\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4A\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x51\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4D\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x29\x2B\x67\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x34\x38\x2B\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x59\x5C\x27\x2B\x34\x39\x2B\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x49\x5C\x27\x29\x29\x2B\x34\x37\x2B\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x78\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x49\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x34\x5C\x27\x29\x29\x2B\x34\x61\x2B\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x29\x2C\x64\x2B\x3D\x32\x56\x7D\x64\x2B\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x4C\x5C\x27\x29\x7D\x7D\x31\x36\x20\x64\x3D\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4D\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x49\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x44\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x4C\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x53\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x59\x5C\x27\x3B\x68\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x64\x29\x2C\x68\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x41\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x31\x74\x5C\x5C\x5A\x5C\x5C\x5A\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x79\x5C\x27\x5D\x28\x29\x7D\x7D\x29\x7D\x31\x36\x20\x36\x53\x3D\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x34\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x44\x5C\x27\x29\x2B\x36\x54\x2B\x28\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4D\x5C\x27\x29\x2B\x6C\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x32\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x29\x2B\x36\x55\x7D\x7D\x24\x28\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x35\x5C\x27\x29\x2B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x33\x5C\x27\x29\x29\x5B\x6F\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x64\x3D\x6F\x3B\x58\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x49\x5C\x27\x29\x21\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x49\x5C\x27\x29\x29\x31\x63\x20\x36\x56\x3D\x36\x57\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x33\x5C\x27\x29\x2C\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4C\x5C\x27\x29\x29\x2C\x36\x58\x3D\x36\x59\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x54\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x56\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x41\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2C\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x79\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x53\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x35\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x78\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x53\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x51\x5C\x5C\x31\x31\x5C\x5C\x31\x4B\x5C\x5C\x41\x5C\x5C\x31\x34\x5C\x5C\x4C\x5C\x5C\x51\x5C\x5C\x31\x5C\x5C\x4E\x5C\x5C\x31\x6D\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x53\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x36\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x31\x5C\x27\x29\x29\x2C\x36\x5A\x3B\x31\x36\x7B\x50\x20\x65\x3D\x37\x30\x2C\x37\x31\x3D\x37\x32\x2C\x34\x62\x3D\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x79\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x53\x5C\x27\x29\x2C\x34\x63\x3D\x24\x28\x37\x33\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x42\x5C\x27\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x29\x2C\x34\x64\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x44\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x31\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x32\x4D\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x46\x5C\x5C\x4E\x5C\x5C\x42\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x79\x5C\x27\x29\x2B\x34\x63\x2B\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x4A\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x29\x2C\x32\x43\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x5A\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x46\x5C\x27\x2B\x65\x3B\x58\x28\x65\x3D\x3D\x5C\x27\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x29\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x4B\x5C\x27\x29\x21\x3D\x3D\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x79\x5C\x5C\x41\x5C\x5C\x31\x4C\x5C\x5C\x31\x48\x5C\x27\x3F\x37\x34\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x2B\x37\x35\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x29\x3E\x3D\x37\x36\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x5D\x26\x26\x28\x37\x37\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x34\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x2C\x37\x38\x29\x2C\x37\x39\x28\x29\x29\x3A\x24\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x32\x43\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x29\x3B\x31\x36\x7B\x58\x28\x65\x3D\x3D\x5C\x27\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x31\x6F\x5C\x5C\x4F\x5C\x5C\x38\x5C\x27\x29\x7B\x58\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x21\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x33\x5C\x27\x29\x29\x7B\x50\x20\x66\x3D\x37\x61\x28\x31\x35\x29\x3B\x66\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x2C\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x36\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x42\x5C\x27\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4B\x5C\x27\x29\x2C\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x51\x5C\x27\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x31\x6A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x31\x61\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x34\x5C\x27\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x34\x5C\x27\x29\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x5C\x43\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x79\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x38\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x4A\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x78\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x44\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x51\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x51\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x78\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x41\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4A\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x33\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x36\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x31\x61\x5C\x5C\x4E\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x29\x29\x7D\x31\x36\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x64\x3B\x58\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x66\x5C\x5C\x35\x5C\x5C\x31\x76\x5C\x5C\x31\x70\x5C\x27\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x31\x5C\x27\x29\x29\x7B\x50\x20\x62\x3D\x32\x57\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x53\x5C\x27\x29\x29\x3B\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x35\x5C\x27\x29\x5D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x4C\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x33\x5C\x27\x29\x2C\x62\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x5A\x5C\x5C\x45\x5C\x5C\x78\x5C\x27\x5D\x3D\x21\x21\x5B\x5D\x2C\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x27\x2B\x37\x62\x2B\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x4A\x5C\x27\x29\x29\x2C\x28\x32\x57\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x44\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x29\x5B\x31\x37\x5D\x7C\x7C\x32\x57\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x41\x5C\x5C\x5A\x5C\x5C\x31\x61\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x31\x78\x5C\x5C\x36\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x31\x37\x5D\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x7A\x5C\x27\x2B\x5C\x27\x5C\x5C\x79\x5C\x27\x5D\x28\x62\x29\x7D\x31\x36\x7B\x50\x20\x63\x3D\x37\x63\x28\x31\x35\x29\x2C\x32\x68\x3D\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x2C\x34\x65\x3D\x32\x68\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x31\x66\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x62\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x29\x2C\x32\x58\x3D\x37\x64\x28\x32\x68\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x29\x2C\x32\x59\x3D\x37\x65\x28\x32\x68\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x29\x2C\x32\x5A\x3D\x37\x66\x28\x32\x68\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x29\x3B\x34\x65\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x34\x5C\x27\x29\x29\x26\x26\x31\x37\x21\x3D\x32\x58\x26\x26\x28\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x32\x58\x29\x2C\x31\x37\x21\x3D\x32\x59\x26\x26\x63\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x32\x59\x29\x2C\x31\x37\x21\x3D\x32\x5A\x26\x26\x63\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x78\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x34\x5C\x27\x29\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x2B\x32\x5A\x2B\x5C\x27\x5C\x5C\x31\x49\x5C\x27\x29\x29\x7D\x7D\x28\x29\x29\x2C\x24\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x79\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x27\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x2C\x24\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x34\x62\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x32\x43\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x29\x7D\x31\x36\x7B\x58\x28\x65\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x4D\x5C\x27\x29\x29\x7B\x58\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x41\x5C\x27\x29\x21\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x41\x5C\x27\x29\x29\x7B\x50\x20\x67\x3D\x37\x67\x5B\x37\x68\x5D\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x44\x5C\x5C\x51\x5C\x27\x29\x5D\x5B\x31\x37\x5D\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4A\x5C\x27\x29\x5D\x5B\x5C\x27\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x27\x5D\x2C\x34\x66\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x4D\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x36\x5C\x5C\x59\x5C\x27\x2B\x67\x2B\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x53\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x29\x3B\x31\x63\x20\x34\x66\x7D\x31\x36\x20\x24\x28\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x6C\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4A\x5C\x27\x29\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x44\x5C\x27\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x2C\x24\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x34\x64\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x32\x43\x29\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x5D\x28\x29\x7D\x31\x36\x20\x65\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x44\x5C\x27\x29\x3F\x24\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x44\x5C\x27\x29\x5D\x28\x29\x3A\x5C\x27\x5C\x5C\x31\x66\x5C\x5C\x31\x4D\x5C\x5C\x31\x79\x5C\x5C\x31\x34\x5C\x5C\x31\x45\x5C\x27\x3D\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4A\x5C\x27\x29\x3F\x37\x69\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x37\x6A\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x29\x3A\x24\x28\x31\x35\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x38\x5C\x27\x2B\x5C\x27\x5C\x5C\x5A\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x36\x5C\x27\x2B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x79\x5C\x27\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4B\x5C\x27\x29\x5D\x28\x29\x7D\x7D\x7D\x7D\x29\x7D\x29\x29\x3B\x31\x30\x20\x32\x35\x28\x61\x2C\x62\x2C\x63\x29\x7B\x50\x20\x64\x3D\x31\x6E\x3B\x32\x31\x28\x50\x20\x65\x3D\x61\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x7A\x5C\x27\x29\x2C\x33\x30\x3D\x2F\x5B\x5E\x7B\x5C\x5C\x7D\x5D\x2B\x28\x3F\x3D\x7D\x29\x2F\x67\x2C\x32\x44\x3D\x31\x37\x3B\x32\x44\x3C\x65\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x5D\x3B\x32\x44\x2B\x2B\x29\x7B\x58\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4C\x5C\x27\x29\x21\x3D\x3D\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x4C\x5C\x27\x29\x29\x37\x6B\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x36\x5C\x27\x29\x29\x3B\x31\x36\x7B\x50\x20\x66\x3D\x65\x5B\x32\x44\x5D\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4B\x5C\x5C\x51\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x33\x5C\x27\x29\x3B\x58\x28\x66\x5B\x31\x37\x5D\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x48\x5C\x27\x5D\x28\x29\x3D\x3D\x62\x29\x31\x63\x20\x32\x62\x21\x3D\x28\x63\x3D\x66\x5B\x31\x65\x5D\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x33\x30\x29\x26\x26\x37\x6C\x28\x63\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x33\x30\x29\x29\x5B\x64\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x7D\x7D\x31\x63\x21\x31\x65\x7D\x31\x30\x20\x31\x4A\x28\x64\x2C\x65\x29\x7B\x50\x20\x66\x3D\x32\x61\x28\x29\x3B\x31\x63\x20\x31\x4A\x3D\x31\x30\x28\x61\x2C\x62\x29\x7B\x61\x3D\x61\x2D\x37\x6D\x3B\x50\x20\x63\x3D\x66\x5B\x61\x5D\x3B\x31\x63\x20\x63\x7D\x2C\x31\x4A\x28\x64\x2C\x65\x29\x7D\x24\x28\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x36\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x6E\x2C\x32\x69\x3D\x24\x28\x31\x35\x29\x2C\x32\x6A\x3D\x32\x69\x5B\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x27\x5D\x28\x29\x2C\x34\x67\x3D\x32\x6A\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x29\x2C\x33\x31\x3D\x32\x35\x28\x32\x6A\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x29\x2C\x33\x32\x3D\x32\x35\x28\x32\x6A\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x51\x5C\x27\x29\x29\x2C\x33\x33\x3D\x32\x35\x28\x32\x6A\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x44\x5C\x27\x29\x29\x3B\x34\x67\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x34\x5C\x27\x29\x29\x26\x26\x31\x37\x21\x3D\x33\x31\x26\x26\x28\x32\x69\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x41\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x33\x31\x29\x2C\x31\x37\x21\x3D\x33\x32\x26\x26\x32\x69\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x33\x32\x29\x2C\x31\x37\x21\x3D\x33\x33\x26\x26\x32\x69\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x78\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x49\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x31\x64\x5C\x27\x2B\x33\x33\x2B\x5C\x27\x5C\x5C\x31\x49\x5C\x27\x29\x29\x7D\x29\x2C\x24\x28\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x41\x5C\x27\x29\x5B\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x66\x3D\x31\x6E\x2C\x32\x45\x3D\x24\x28\x31\x35\x29\x2C\x31\x5A\x3D\x32\x45\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x2C\x33\x34\x3D\x31\x5A\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x29\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x2C\x32\x46\x3D\x7B\x7D\x3B\x32\x46\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x41\x5C\x27\x29\x5D\x3D\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x41\x5C\x27\x29\x2C\x32\x46\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4D\x5C\x27\x29\x5D\x3D\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x31\x5C\x27\x29\x2C\x28\x33\x34\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x33\x5C\x27\x29\x29\x26\x26\x28\x31\x5A\x3D\x31\x37\x21\x3D\x32\x35\x28\x31\x5A\x2C\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x29\x3F\x32\x35\x28\x31\x5A\x2C\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x31\x5C\x27\x29\x29\x3A\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x51\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x41\x5C\x27\x29\x2C\x32\x45\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x33\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x79\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4A\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x35\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x4D\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x36\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x31\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x4C\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x31\x5C\x5C\x4D\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x33\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x33\x5C\x27\x29\x2B\x31\x5A\x2B\x28\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x27\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x79\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x31\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x49\x5C\x27\x29\x29\x2B\x31\x5A\x2B\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x4B\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x51\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x79\x5C\x5C\x49\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x4A\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x49\x5C\x27\x29\x29\x29\x2C\x24\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x31\x30\x28\x62\x29\x7B\x50\x20\x63\x3D\x66\x3B\x58\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x51\x5C\x27\x29\x3D\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x34\x5C\x27\x29\x29\x31\x63\x20\x37\x6E\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x29\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x78\x5C\x5C\x4C\x5C\x27\x29\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x55\x5C\x5C\x31\x7A\x5C\x27\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x31\x6A\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x76\x5C\x27\x2B\x5C\x27\x5C\x5C\x42\x5C\x27\x5D\x28\x37\x6F\x29\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x55\x5C\x5C\x31\x7A\x5C\x27\x29\x3B\x31\x36\x28\x62\x3D\x24\x28\x31\x35\x29\x29\x5B\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x5D\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4B\x5C\x27\x29\x2C\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x63\x3B\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x79\x5C\x27\x29\x2C\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4D\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x27\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x31\x57\x29\x7D\x29\x7D\x29\x2C\x24\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4D\x5C\x27\x29\x29\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x32\x46\x29\x2C\x24\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x35\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x36\x5C\x27\x29\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x62\x29\x7B\x50\x20\x63\x3D\x66\x3B\x58\x28\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x35\x5C\x27\x29\x21\x3D\x3D\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x35\x5C\x27\x29\x29\x7B\x50\x20\x64\x3D\x37\x70\x5B\x5C\x27\x5C\x5C\x35\x5C\x5C\x31\x6F\x5C\x27\x5D\x28\x37\x71\x2B\x31\x65\x29\x2C\x34\x68\x3D\x64\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x34\x68\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x29\x5D\x28\x31\x37\x29\x3D\x3D\x3D\x5C\x27\x5C\x5C\x31\x72\x5C\x27\x29\x7B\x50\x20\x65\x3D\x37\x72\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x27\x29\x5D\x28\x29\x3B\x65\x5B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x4A\x5C\x27\x29\x2B\x63\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x34\x5C\x27\x29\x29\x7D\x7D\x31\x36\x28\x62\x3D\x24\x28\x31\x35\x29\x29\x5B\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x63\x3B\x31\x63\x20\x24\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x79\x5C\x27\x29\x29\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x27\x5D\x28\x7B\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x3A\x24\x28\x62\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x29\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x5D\x2D\x33\x69\x7D\x2C\x31\x54\x29\x2C\x21\x31\x65\x7D\x29\x7D\x29\x29\x2C\x33\x34\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x78\x5C\x5C\x4B\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x48\x5C\x5C\x31\x69\x5C\x27\x29\x26\x26\x28\x32\x45\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x31\x67\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x79\x5C\x5C\x44\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4D\x5C\x27\x29\x29\x2C\x24\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x35\x5C\x27\x29\x2B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4D\x5C\x5C\x53\x5C\x27\x29\x5D\x28\x24\x28\x66\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x48\x5C\x5C\x33\x5C\x27\x29\x29\x29\x29\x7D\x29\x2C\x24\x28\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x4C\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x52\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x5C\x31\x6F\x5C\x5C\x4F\x5C\x5C\x76\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x29\x5B\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x6E\x2C\x31\x53\x3D\x24\x28\x31\x35\x29\x2C\x32\x36\x3D\x31\x53\x5B\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x27\x5D\x28\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x29\x2C\x32\x37\x3D\x31\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x33\x5C\x27\x29\x5D\x28\x29\x3B\x58\x28\x32\x36\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4B\x5C\x5C\x33\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x69\x5C\x27\x29\x29\x7B\x58\x28\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x39\x5C\x5C\x79\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x3D\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x41\x5C\x27\x29\x29\x7B\x31\x58\x20\x34\x69\x3D\x32\x37\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x31\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x3B\x31\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x31\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x2B\x34\x69\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x29\x7D\x31\x36\x7B\x58\x28\x37\x73\x29\x7B\x50\x20\x62\x3D\x37\x74\x5B\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x5A\x5C\x27\x5D\x28\x37\x75\x2C\x32\x47\x29\x3B\x31\x63\x20\x37\x76\x3D\x32\x62\x2C\x62\x7D\x7D\x7D\x58\x28\x32\x36\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x36\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x69\x5C\x27\x29\x29\x7B\x31\x58\x20\x34\x6A\x3D\x32\x37\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x78\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x3B\x31\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x4D\x5C\x27\x29\x2B\x34\x6A\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x29\x7D\x58\x28\x32\x36\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x49\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x31\x69\x5C\x27\x29\x29\x7B\x31\x58\x20\x34\x6B\x3D\x32\x37\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x33\x5C\x5C\x31\x5C\x27\x29\x2C\x5C\x27\x5C\x27\x29\x3B\x31\x53\x5B\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x31\x67\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x51\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x59\x5C\x27\x2B\x34\x6B\x2B\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x27\x29\x7D\x58\x28\x32\x36\x5B\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x31\x69\x5C\x27\x29\x29\x7B\x58\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x21\x3D\x3D\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x4C\x5C\x27\x29\x29\x37\x77\x3D\x37\x78\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x36\x5C\x27\x29\x2C\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4C\x5C\x5C\x4D\x5C\x27\x29\x29\x3B\x31\x36\x7B\x31\x58\x20\x34\x6C\x3D\x32\x37\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x4A\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x42\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x27\x29\x3B\x31\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x34\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x31\x5C\x27\x29\x2B\x34\x6C\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x35\x5C\x5C\x33\x5C\x27\x29\x29\x7D\x7D\x58\x28\x32\x36\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x32\x5C\x5C\x31\x69\x5C\x27\x29\x29\x7B\x31\x58\x20\x34\x6D\x3D\x32\x37\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x78\x5C\x5C\x49\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x4B\x5C\x27\x29\x2C\x5C\x27\x5C\x27\x29\x3B\x31\x53\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x41\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x4E\x5C\x27\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x31\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x4D\x5C\x27\x29\x2B\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2B\x34\x6D\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x36\x5C\x5C\x4B\x5C\x27\x29\x29\x7D\x7D\x29\x2C\x24\x28\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x41\x5C\x27\x29\x2B\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x36\x5C\x5C\x4B\x5C\x27\x29\x29\x5B\x31\x6E\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x41\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x31\x30\x28\x29\x7B\x50\x20\x61\x3D\x31\x6E\x2C\x33\x35\x3D\x24\x28\x31\x35\x29\x3B\x33\x35\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x34\x5C\x27\x29\x5D\x28\x5C\x27\x5C\x5C\x38\x5C\x5C\x42\x5C\x5C\x78\x5C\x27\x29\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x4A\x5C\x5C\x36\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x53\x5C\x5C\x35\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x53\x5C\x27\x29\x29\x26\x26\x33\x35\x5B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x4D\x5C\x27\x29\x5D\x28\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x49\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x35\x5C\x5C\x78\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x49\x5C\x5C\x41\x5C\x27\x29\x2B\x61\x28\x5C\x27\x5C\x5C\x31\x5C\x5C\x32\x5C\x5C\x33\x5C\x5C\x41\x5C\x5C\x51\x5C\x27\x29\x29\x7D\x29\x3B\x31\x30\x20\x32\x61\x28\x29\x7B\x50\x20\x61\x3D\x5B\x5C\x27\x5C\x5C\x44\x5C\x5C\x35\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x31\x6C\x5C\x5C\x55\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x46\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x54\x5C\x5C\x31\x44\x5C\x5C\x31\x6A\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x31\x31\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x66\x5C\x5C\x4C\x5C\x5C\x31\x75\x5C\x5C\x31\x6D\x5C\x5C\x56\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x31\x62\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x31\x70\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x31\x67\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x5C\x44\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x41\x5C\x5C\x5A\x5C\x5C\x31\x61\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x31\x78\x5C\x5C\x36\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x67\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x51\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x54\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x41\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x31\x6A\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x31\x6C\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x56\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x41\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x55\x5C\x5C\x31\x76\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x79\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x31\x67\x5C\x5C\x79\x5C\x5C\x48\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x4E\x5C\x5C\x34\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x39\x5C\x5C\x79\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x5A\x5C\x5C\x31\x6A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x75\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x6C\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x5C\x41\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x62\x5C\x5C\x5A\x5C\x5C\x31\x41\x5C\x5C\x31\x62\x5C\x5C\x32\x66\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x31\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x54\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x41\x5C\x5C\x31\x39\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x31\x64\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x31\x34\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x76\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x55\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6D\x5C\x5C\x31\x76\x5C\x5C\x31\x77\x5C\x5C\x36\x5C\x5C\x31\x75\x5C\x27\x2C\x5C\x27\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x31\x79\x5C\x5C\x47\x5C\x5C\x31\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x66\x5C\x5C\x31\x67\x5C\x5C\x4F\x5C\x5C\x31\x59\x5C\x5C\x31\x73\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x31\x6C\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x46\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x4C\x5C\x5C\x31\x5C\x5C\x56\x5C\x5C\x31\x46\x5C\x5C\x4F\x5C\x5C\x31\x77\x5C\x5C\x31\x66\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x5A\x5C\x5C\x45\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x52\x5C\x5C\x31\x70\x5C\x5C\x76\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x31\x31\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x4E\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x31\x61\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x32\x42\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x4B\x5C\x5C\x53\x5C\x5C\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x52\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x49\x5C\x5C\x4A\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x31\x66\x5C\x5C\x36\x5C\x5C\x41\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x36\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6F\x5C\x5C\x31\x74\x5C\x5C\x31\x73\x5C\x5C\x31\x46\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x79\x5C\x5C\x31\x39\x5C\x5C\x32\x66\x5C\x5C\x76\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x44\x5C\x5C\x78\x5C\x5C\x31\x67\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x31\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x31\x45\x5C\x5C\x7A\x5C\x5C\x31\x74\x5C\x5C\x32\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x46\x5C\x5C\x31\x44\x5C\x5C\x31\x51\x5C\x5C\x31\x78\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x45\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x52\x5C\x5C\x41\x5C\x5C\x37\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x33\x5C\x5C\x31\x51\x5C\x5C\x38\x5C\x5C\x31\x67\x5C\x5C\x31\x79\x5C\x5C\x44\x5C\x5C\x34\x5C\x5C\x31\x47\x5C\x5C\x31\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x5C\x31\x6C\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x62\x5C\x5C\x31\x6A\x5C\x5C\x31\x70\x5C\x5C\x5A\x5C\x5C\x31\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x64\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x31\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x5C\x53\x5C\x5C\x31\x48\x5C\x5C\x44\x5C\x5C\x31\x76\x5C\x5C\x47\x5C\x5C\x32\x66\x5C\x5C\x31\x4D\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x76\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x31\x75\x5C\x5C\x35\x5C\x5C\x31\x31\x5C\x5C\x31\x74\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x75\x5C\x5C\x38\x5C\x5C\x31\x76\x5C\x5C\x31\x61\x5C\x5C\x31\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x52\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x46\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x41\x5C\x5C\x31\x34\x5C\x5C\x31\x78\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x44\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x67\x5C\x5C\x31\x51\x5C\x5C\x78\x5C\x5C\x31\x46\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6D\x5C\x5C\x49\x5C\x5C\x56\x5C\x5C\x31\x44\x5C\x5C\x31\x78\x5C\x5C\x4D\x5C\x5C\x45\x5C\x5C\x31\x47\x5C\x5C\x31\x38\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x55\x5C\x5C\x54\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x79\x5C\x5C\x35\x5C\x5C\x31\x73\x5C\x5C\x76\x5C\x5C\x31\x6F\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x51\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x54\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x6A\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x55\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x34\x5C\x5C\x31\x6C\x5C\x5C\x4E\x5C\x5C\x4D\x5C\x5C\x31\x6C\x5C\x5C\x4E\x5C\x5C\x49\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x31\x34\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x31\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x31\x74\x5C\x5C\x5A\x5C\x5C\x5A\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x39\x5C\x5C\x31\x59\x5C\x5C\x31\x67\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x36\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x55\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x31\x34\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x31\x6F\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x31\x72\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x45\x5C\x5C\x31\x5C\x5C\x56\x5C\x5C\x31\x45\x5C\x5C\x31\x48\x5C\x5C\x4B\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x44\x5C\x5C\x44\x5C\x5C\x31\x5C\x5C\x31\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x52\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x4D\x5C\x5C\x34\x5C\x5C\x4C\x5C\x5C\x4A\x5C\x5C\x31\x5C\x5C\x31\x5C\x5C\x51\x5C\x5C\x5A\x5C\x5C\x78\x5C\x5C\x31\x6D\x5C\x5C\x31\x44\x5C\x5C\x31\x48\x5C\x5C\x31\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x79\x5C\x5C\x41\x5C\x5C\x31\x4C\x5C\x5C\x31\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x31\x4D\x5C\x5C\x31\x6D\x5C\x5C\x31\x34\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x52\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x67\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x73\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x4B\x5C\x5C\x31\x47\x5C\x5C\x31\x39\x5C\x5C\x31\x70\x5C\x5C\x31\x61\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x31\x64\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x5C\x32\x4D\x5C\x5C\x31\x69\x5C\x5C\x55\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x38\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x52\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x36\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x31\x33\x5C\x5C\x31\x76\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x31\x6A\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x31\x66\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x31\x66\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x44\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x7A\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x77\x5C\x5C\x4F\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x37\x5C\x5C\x33\x37\x5C\x5C\x33\x37\x5C\x5C\x55\x5C\x5C\x31\x55\x5C\x5C\x33\x38\x5C\x5C\x31\x55\x5C\x5C\x33\x38\x5C\x5C\x31\x55\x5C\x5C\x33\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x5C\x5C\x45\x5C\x5C\x31\x62\x5C\x5C\x31\x6D\x5C\x5C\x56\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x54\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x31\x79\x5C\x5C\x31\x6D\x5C\x5C\x35\x5C\x5C\x32\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x33\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x47\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x31\x31\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x78\x5C\x5C\x31\x46\x5C\x5C\x76\x5C\x5C\x31\x78\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x70\x5C\x5C\x7A\x5C\x5C\x31\x73\x5C\x5C\x35\x5C\x5C\x31\x70\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x31\x46\x5C\x5C\x31\x6A\x5C\x5C\x31\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x5C\x32\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x79\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x31\x62\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x54\x5C\x5C\x43\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x4E\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x6B\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x31\x64\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x73\x5C\x5C\x42\x5C\x5C\x42\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x52\x5C\x5C\x31\x32\x5C\x5C\x43\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x38\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x31\x45\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x41\x5C\x5C\x35\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x67\x5C\x5C\x4D\x5C\x5C\x31\x74\x5C\x5C\x31\x38\x5C\x5C\x31\x66\x5C\x5C\x31\x44\x5C\x5C\x31\x5C\x5C\x33\x5C\x5C\x31\x73\x5C\x5C\x31\x39\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x45\x5C\x5C\x76\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x77\x5C\x5C\x31\x74\x5C\x5C\x31\x31\x5C\x5C\x36\x5C\x5C\x31\x6F\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x31\x45\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x42\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x64\x5C\x5C\x31\x49\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x31\x66\x5C\x5C\x76\x5C\x5C\x31\x44\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x5C\x45\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x31\x68\x5C\x5C\x48\x5C\x5C\x5A\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x77\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x77\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x31\x4D\x5C\x5C\x43\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x6C\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x47\x5C\x5C\x38\x5C\x5C\x31\x64\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x31\x31\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x74\x5C\x5C\x35\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x49\x5C\x5C\x51\x5C\x5C\x78\x5C\x5C\x31\x48\x5C\x5C\x31\x42\x5C\x5C\x32\x5C\x5C\x41\x5C\x5C\x31\x4C\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x42\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x31\x6F\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x41\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x43\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x59\x5C\x5C\x52\x5C\x5C\x7A\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x41\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x37\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x31\x67\x5C\x5C\x4C\x5C\x5C\x35\x5C\x5C\x31\x62\x5C\x5C\x47\x5C\x5C\x38\x5C\x5C\x53\x5C\x5C\x31\x78\x5C\x5C\x31\x66\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x36\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x32\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x31\x66\x5C\x5C\x35\x5C\x5C\x31\x76\x5C\x5C\x31\x70\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x76\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x46\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x75\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x46\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x46\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x7A\x5C\x5C\x31\x6C\x5C\x5C\x52\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x4B\x5C\x5C\x34\x5C\x5C\x51\x5C\x5C\x4A\x5C\x5C\x4B\x5C\x5C\x4D\x5C\x5C\x41\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x31\x74\x5C\x5C\x31\x34\x5C\x5C\x31\x67\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x31\x6A\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x4D\x5C\x5C\x4A\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x31\x38\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x76\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x39\x5C\x5C\x31\x45\x5C\x5C\x31\x79\x5C\x5C\x38\x5C\x5C\x56\x5C\x5C\x31\x4C\x5C\x5C\x78\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x64\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x46\x5C\x5C\x31\x61\x5C\x5C\x31\x42\x5C\x5C\x31\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x42\x5C\x5C\x31\x74\x5C\x5C\x79\x5C\x5C\x4E\x5C\x5C\x31\x6D\x5C\x27\x2C\x5C\x27\x5C\x5C\x51\x5C\x5C\x31\x31\x5C\x5C\x31\x4B\x5C\x5C\x41\x5C\x5C\x31\x34\x5C\x5C\x4C\x5C\x5C\x51\x5C\x5C\x31\x5C\x5C\x4E\x5C\x5C\x31\x6D\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x31\x62\x5C\x5C\x4E\x5C\x5C\x79\x5C\x5C\x31\x70\x5C\x5C\x31\x34\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x4E\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x32\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x4A\x5C\x5C\x49\x5C\x5C\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x6D\x5C\x5C\x45\x5C\x5C\x31\x4D\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x5C\x31\x42\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x45\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x36\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x46\x5C\x5C\x31\x38\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x76\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x44\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x45\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x31\x6D\x5C\x5C\x49\x5C\x5C\x31\x79\x5C\x5C\x31\x62\x5C\x5C\x31\x6D\x5C\x5C\x42\x5C\x5C\x31\x31\x5C\x5C\x31\x73\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x53\x5C\x5C\x4D\x5C\x5C\x42\x5C\x5C\x31\x6D\x5C\x5C\x31\x72\x5C\x5C\x38\x5C\x5C\x4C\x5C\x5C\x7A\x5C\x5C\x31\x66\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x67\x5C\x5C\x31\x73\x5C\x5C\x31\x4D\x5C\x5C\x31\x67\x5C\x5C\x31\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x38\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x33\x5C\x5C\x51\x5C\x5C\x4C\x5C\x5C\x31\x44\x5C\x5C\x36\x5C\x5C\x31\x42\x5C\x5C\x31\x61\x5C\x5C\x38\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x36\x5C\x5C\x52\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x5C\x31\x64\x5C\x5C\x44\x5C\x5C\x43\x5C\x5C\x42\x5C\x5C\x38\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x31\x62\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x43\x5C\x5C\x36\x5C\x5C\x31\x6A\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x44\x5C\x5C\x35\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x38\x5C\x5C\x56\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x54\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x31\x62\x5C\x5C\x4E\x5C\x5C\x43\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x6B\x5C\x5C\x44\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x4D\x5C\x5C\x31\x6F\x5C\x5C\x31\x61\x5C\x5C\x31\x79\x5C\x5C\x31\x77\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x31\x51\x5C\x5C\x78\x5C\x5C\x31\x79\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x36\x5C\x5C\x31\x7A\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x37\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x31\x6A\x5C\x5C\x31\x70\x5C\x5C\x31\x38\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x52\x5C\x5C\x7A\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x46\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x57\x5C\x5C\x52\x5C\x5C\x79\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x56\x5C\x5C\x47\x5C\x5C\x37\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x31\x4D\x5C\x5C\x31\x79\x5C\x5C\x31\x34\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x41\x5C\x5C\x76\x5C\x5C\x32\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x38\x5C\x5C\x31\x38\x5C\x5C\x31\x6A\x5C\x5C\x31\x42\x5C\x5C\x31\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x6C\x5C\x27\x2C\x5C\x27\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x31\x78\x5C\x5C\x36\x5C\x5C\x36\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x31\x6C\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x31\x31\x5C\x5C\x31\x31\x5C\x5C\x55\x5C\x5C\x5A\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x4F\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x31\x61\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x31\x69\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x31\x41\x5C\x5C\x32\x5C\x5C\x31\x34\x5C\x5C\x31\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x31\x41\x5C\x5C\x31\x6F\x5C\x5C\x31\x4B\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x79\x5C\x5C\x46\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6A\x5C\x5C\x31\x66\x5C\x5C\x31\x46\x5C\x5C\x4E\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x4E\x5C\x5C\x34\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x41\x5C\x5C\x35\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x5C\x31\x73\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x78\x5C\x5C\x78\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x48\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x59\x5C\x5C\x31\x73\x5C\x5C\x42\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x31\x64\x5C\x5C\x52\x5C\x5C\x31\x78\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x61\x5C\x5C\x36\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x76\x5C\x5C\x44\x5C\x5C\x52\x5C\x5C\x31\x62\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x31\x74\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x54\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x5C\x54\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x34\x5C\x5C\x4A\x5C\x5C\x51\x5C\x5C\x4B\x5C\x5C\x49\x5C\x5C\x31\x42\x5C\x5C\x37\x5C\x5C\x48\x5C\x5C\x31\x76\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x31\x66\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x31\x62\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x38\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x36\x5C\x5C\x32\x42\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x32\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x5C\x48\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x76\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x42\x5C\x5C\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x31\x45\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x5C\x33\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x6B\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x31\x69\x5C\x27\x2C\x5C\x27\x5C\x5C\x5A\x5C\x5C\x38\x5C\x5C\x31\x51\x5C\x5C\x31\x6F\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x46\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x43\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x36\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x52\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x70\x5C\x5C\x31\x31\x5C\x5C\x31\x62\x5C\x5C\x31\x70\x5C\x5C\x31\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x47\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x31\x41\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x76\x5C\x5C\x38\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x4B\x5C\x5C\x51\x5C\x5C\x4B\x5C\x5C\x33\x5C\x5C\x31\x5C\x5C\x31\x31\x5C\x5C\x31\x73\x5C\x5C\x41\x5C\x5C\x41\x5C\x5C\x31\x4B\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x31\x31\x5C\x5C\x7A\x5C\x5C\x31\x62\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x4F\x5C\x5C\x38\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x31\x31\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x44\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x57\x5C\x5C\x56\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x52\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x27\x2C\x5C\x27\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x7A\x5C\x5C\x7A\x5C\x5C\x31\x61\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x31\x49\x5C\x5C\x52\x5C\x5C\x31\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x31\x73\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x4F\x5C\x5C\x48\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x73\x5C\x5C\x32\x66\x5C\x5C\x38\x5C\x5C\x54\x5C\x5C\x31\x4B\x5C\x27\x2C\x5C\x27\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x54\x5C\x5C\x55\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x48\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x37\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x52\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x78\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x46\x5C\x5C\x31\x31\x5C\x5C\x42\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x34\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x48\x5C\x5C\x52\x5C\x5C\x31\x68\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x42\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x36\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x59\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x4F\x5C\x5C\x41\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x38\x5C\x5C\x4A\x5C\x5C\x4A\x5C\x5C\x46\x5C\x5C\x42\x5C\x5C\x56\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x36\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x31\x39\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x4F\x5C\x5C\x31\x62\x5C\x5C\x31\x76\x5C\x5C\x31\x44\x5C\x5C\x54\x5C\x5C\x31\x46\x5C\x5C\x31\x70\x5C\x5C\x31\x6D\x5C\x5C\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x4B\x5C\x5C\x49\x5C\x5C\x53\x5C\x5C\x34\x5C\x5C\x34\x5C\x5C\x49\x5C\x5C\x31\x5C\x5C\x79\x5C\x5C\x31\x79\x5C\x5C\x35\x5C\x5C\x31\x59\x5C\x5C\x31\x66\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x37\x5C\x5C\x31\x64\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x37\x5C\x5C\x31\x69\x5C\x5C\x55\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x68\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x31\x34\x5C\x5C\x46\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x31\x64\x5C\x5C\x51\x5C\x5C\x51\x5C\x5C\x31\x4E\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x5A\x5C\x5C\x7A\x5C\x5C\x35\x5C\x5C\x59\x5C\x5C\x55\x5C\x5C\x43\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x37\x5C\x5C\x7A\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x46\x5C\x5C\x44\x5C\x5C\x76\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x43\x5C\x5C\x78\x5C\x5C\x46\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x76\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x54\x5C\x5C\x57\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x31\x74\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x5A\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x37\x5C\x5C\x4E\x5C\x5C\x76\x5C\x5C\x42\x5C\x27\x2C\x5C\x27\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x48\x5C\x5C\x76\x5C\x5C\x41\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x77\x5C\x5C\x31\x45\x5C\x5C\x48\x5C\x5C\x31\x73\x5C\x5C\x31\x73\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x47\x5C\x5C\x47\x5C\x5C\x7A\x5C\x5C\x5A\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x38\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x42\x5C\x5C\x78\x5C\x5C\x4E\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x79\x5C\x5C\x31\x67\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x38\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x36\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x47\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x31\x34\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x31\x45\x5C\x5C\x35\x5C\x5C\x44\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x76\x5C\x5C\x36\x5C\x5C\x79\x5C\x5C\x52\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x38\x5C\x5C\x43\x5C\x5C\x31\x74\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x79\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x41\x5C\x5C\x76\x5C\x5C\x32\x5C\x27\x2C\x5C\x27\x5C\x5C\x4C\x5C\x5C\x31\x6A\x5C\x5C\x31\x5C\x5C\x76\x5C\x5C\x4E\x5C\x5C\x4D\x5C\x5C\x4C\x5C\x5C\x49\x5C\x5C\x31\x4C\x5C\x5C\x31\x70\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x48\x5C\x5C\x35\x5C\x5C\x45\x5C\x5C\x4F\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x72\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x4F\x5C\x5C\x7A\x5C\x5C\x59\x5C\x27\x2C\x5C\x27\x5C\x5C\x4D\x5C\x5C\x4D\x5C\x5C\x31\x5C\x5C\x4B\x5C\x5C\x51\x5C\x5C\x31\x48\x5C\x5C\x41\x5C\x5C\x31\x45\x5C\x5C\x31\x4C\x5C\x5C\x31\x34\x5C\x5C\x31\x4B\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x31\x6A\x5C\x5C\x79\x5C\x5C\x47\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x46\x5C\x5C\x78\x5C\x5C\x76\x5C\x5C\x45\x5C\x5C\x37\x5C\x5C\x36\x5C\x5C\x43\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x4E\x5C\x5C\x33\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x57\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x52\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x56\x5C\x5C\x49\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x47\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x76\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x44\x5C\x5C\x5A\x5C\x5C\x46\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x45\x5C\x5C\x35\x5C\x5C\x42\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x56\x5C\x5C\x31\x31\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x4E\x5C\x5C\x4C\x5C\x5C\x34\x5C\x5C\x46\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x33\x5C\x5C\x53\x5C\x5C\x4B\x5C\x5C\x31\x70\x5C\x5C\x31\x6A\x5C\x5C\x32\x5C\x5C\x31\x75\x5C\x5C\x31\x75\x5C\x5C\x31\x78\x5C\x27\x2C\x5C\x27\x5C\x5C\x31\x74\x5C\x5C\x31\x42\x5C\x5C\x31\x75\x5C\x5C\x31\x4C\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x45\x5C\x5C\x46\x5C\x5C\x38\x5C\x5C\x78\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x47\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x36\x5C\x5C\x52\x5C\x5C\x4E\x5C\x5C\x42\x5C\x5C\x35\x5C\x5C\x44\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x27\x2C\x5C\x27\x5C\x5C\x78\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x38\x5C\x5C\x38\x5C\x5C\x31\x33\x5C\x5C\x57\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x5C\x79\x5C\x5C\x43\x5C\x5C\x31\x34\x5C\x5C\x59\x5C\x5C\x31\x32\x5C\x5C\x56\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x42\x5C\x5C\x43\x5C\x5C\x31\x38\x5C\x5C\x35\x5C\x27\x2C\x5C\x27\x5C\x5C\x37\x5C\x5C\x35\x5C\x5C\x32\x5C\x5C\x37\x5C\x5C\x56\x5C\x5C\x31\x76\x5C\x5C\x36\x5C\x5C\x31\x34\x5C\x5C\x36\x5C\x5C\x38\x5C\x27\x2C\x5C\x27\x5C\x5C\x7A\x5C\x5C\x43\x5C\x5C\x54\x5C\x5C\x4E\x5C\x5C\x37\x5C\x27\x2C\x5C\x27\x5C\x5C\x55\x5C\x5C\x41\x5C\x5C\x36\x5C\x5C\x78\x5C\x5C\x31\x38\x5C\x5C\x46\x5C\x5C\x37\x5C\x5C\x76\x5C\x5C\x47\x5C\x27\x2C\x5C\x27\x5C\x5C\x52\x5C\x5C\x36\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x5C\x45\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x48\x5C\x5C\x54\x5C\x5C\x56\x5C\x5C\x41\x5C\x5C\x7A\x5C\x5C\x36\x5C\x5C\x45\x5C\x5C\x31\x38\x5C\x5C\x55\x5C\x27\x2C\x5C\x27\x5C\x5C\x36\x5C\x5C\x31\x76\x5C\x5C\x36\x5C\x5C\x32\x5C\x27\x2C\x5C\x27\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x52\x5C\x5C\x55\x5C\x5C\x47\x5C\x5C\x76\x5C\x5C\x38\x5C\x5C\x37\x5C\x5C\x46\x5C\x27\x2C\x5C\x27\x5C\x5C\x4E\x5C\x5C\x35\x5C\x5C\x36\x5C\x5C\x79\x5C\x27\x2C\x5C\x27\x5C\x5C\x43\x5C\x5C\x79\x5C\x5C\x54\x5C\x5C\x35\x5C\x5C\x37\x5C\x27\x5D\x3B\x32\x61\x3D\x31\x30\x28\x29\x7B\x31\x63\x20\x61\x7D\x3B\x31\x63\x20\x32\x61\x28\x29\x7D\x27\x2C\x36\x32\x2C\x37\x4B\x2C\x27\x7C\x37\x4C\x7C\x37\x4D\x7C\x37\x4E\x7C\x37\x4F\x7C\x37\x50\x7C\x37\x51\x7C\x37\x52\x7C\x37\x53\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x37\x54\x7C\x7C\x37\x55\x7C\x37\x56\x7C\x37\x57\x7C\x37\x58\x7C\x37\x59\x7C\x37\x5A\x7C\x38\x30\x7C\x38\x31\x7C\x38\x32\x7C\x38\x33\x7C\x38\x34\x7C\x38\x35\x7C\x38\x36\x7C\x38\x37\x7C\x38\x38\x7C\x38\x39\x7C\x38\x61\x7C\x38\x62\x7C\x38\x63\x7C\x38\x64\x7C\x38\x65\x7C\x38\x66\x7C\x38\x67\x7C\x38\x68\x7C\x38\x69\x7C\x38\x6A\x7C\x37\x42\x7C\x38\x6B\x7C\x38\x6C\x7C\x37\x79\x7C\x38\x6D\x7C\x38\x6E\x7C\x38\x6F\x7C\x38\x70\x7C\x38\x71\x7C\x38\x72\x7C\x38\x73\x7C\x38\x74\x7C\x38\x75\x7C\x38\x76\x7C\x38\x77\x7C\x37\x7A\x7C\x38\x78\x7C\x38\x79\x7C\x38\x7A\x7C\x38\x41\x7C\x38\x42\x7C\x38\x43\x7C\x38\x44\x7C\x38\x45\x7C\x38\x46\x7C\x38\x47\x7C\x38\x48\x7C\x38\x49\x7C\x38\x4A\x7C\x38\x4B\x7C\x38\x4C\x7C\x38\x4D\x7C\x38\x4E\x7C\x38\x4F\x7C\x38\x50\x7C\x38\x51\x7C\x38\x52\x7C\x38\x53\x7C\x38\x54\x7C\x38\x55\x7C\x38\x56\x7C\x37\x44\x7C\x38\x57\x7C\x38\x58\x7C\x38\x59\x7C\x38\x5A\x7C\x39\x30\x7C\x39\x31\x7C\x39\x32\x7C\x39\x33\x7C\x39\x34\x7C\x39\x35\x7C\x39\x36\x7C\x39\x37\x7C\x39\x38\x7C\x39\x39\x7C\x39\x61\x7C\x39\x62\x7C\x39\x63\x7C\x39\x64\x7C\x39\x65\x7C\x39\x66\x7C\x39\x67\x7C\x39\x68\x7C\x39\x69\x7C\x39\x6A\x7C\x39\x6B\x7C\x39\x6C\x7C\x39\x6D\x7C\x39\x6E\x7C\x39\x6F\x7C\x39\x70\x7C\x39\x71\x7C\x39\x72\x7C\x39\x73\x7C\x39\x74\x7C\x39\x75\x7C\x39\x76\x7C\x39\x77\x7C\x39\x78\x7C\x39\x79\x7C\x39\x7A\x7C\x39\x41\x7C\x39\x42\x7C\x39\x43\x7C\x39\x44\x7C\x39\x45\x7C\x39\x46\x7C\x39\x47\x7C\x39\x48\x7C\x39\x49\x7C\x39\x4A\x7C\x39\x4B\x7C\x39\x4C\x7C\x39\x4D\x7C\x39\x4E\x7C\x39\x4F\x7C\x39\x50\x7C\x39\x51\x7C\x39\x52\x7C\x39\x53\x7C\x39\x54\x7C\x39\x55\x7C\x39\x56\x7C\x39\x57\x7C\x39\x58\x7C\x39\x59\x7C\x39\x5A\x7C\x61\x30\x7C\x61\x31\x7C\x61\x32\x7C\x61\x33\x7C\x61\x34\x7C\x61\x35\x7C\x61\x36\x7C\x61\x37\x7C\x61\x38\x7C\x61\x39\x7C\x61\x61\x7C\x61\x62\x7C\x61\x63\x7C\x61\x64\x7C\x61\x65\x7C\x61\x66\x7C\x61\x67\x7C\x61\x68\x7C\x61\x69\x7C\x61\x6A\x7C\x61\x6B\x7C\x61\x6C\x7C\x61\x6D\x7C\x61\x6E\x7C\x61\x6F\x7C\x61\x70\x7C\x61\x71\x7C\x61\x72\x7C\x61\x73\x7C\x61\x74\x7C\x61\x75\x7C\x61\x76\x7C\x61\x77\x7C\x61\x78\x7C\x61\x79\x7C\x61\x7A\x7C\x61\x41\x7C\x61\x42\x7C\x61\x43\x7C\x37\x46\x7C\x61\x44\x7C\x61\x45\x7C\x61\x46\x7C\x61\x47\x7C\x61\x48\x7C\x61\x49\x7C\x61\x4A\x7C\x61\x4B\x7C\x61\x4C\x7C\x61\x4D\x7C\x61\x4E\x7C\x61\x4F\x7C\x61\x50\x7C\x61\x51\x7C\x61\x52\x7C\x61\x53\x7C\x61\x54\x7C\x61\x55\x7C\x61\x56\x7C\x61\x57\x7C\x61\x58\x7C\x61\x59\x7C\x61\x5A\x7C\x62\x30\x7C\x62\x31\x7C\x62\x32\x7C\x62\x33\x7C\x62\x34\x7C\x62\x35\x7C\x62\x36\x7C\x62\x37\x7C\x62\x38\x7C\x62\x39\x7C\x62\x61\x7C\x62\x62\x7C\x62\x63\x7C\x62\x64\x7C\x62\x65\x7C\x62\x66\x7C\x62\x67\x7C\x62\x68\x7C\x62\x69\x7C\x62\x6A\x7C\x62\x6B\x7C\x62\x6C\x7C\x62\x6D\x7C\x62\x6E\x7C\x62\x6F\x7C\x62\x70\x7C\x62\x71\x7C\x62\x72\x7C\x62\x73\x7C\x62\x74\x7C\x62\x75\x7C\x62\x76\x7C\x62\x77\x7C\x62\x78\x7C\x62\x79\x7C\x62\x7A\x7C\x62\x41\x7C\x62\x42\x7C\x62\x43\x7C\x62\x44\x7C\x62\x45\x7C\x37\x43\x7C\x62\x46\x7C\x62\x47\x7C\x62\x48\x7C\x62\x49\x7C\x62\x4A\x7C\x62\x4B\x7C\x62\x4C\x7C\x62\x4D\x7C\x62\x4E\x7C\x62\x4F\x7C\x62\x50\x7C\x62\x51\x7C\x62\x52\x7C\x62\x53\x7C\x62\x54\x7C\x62\x55\x7C\x62\x56\x7C\x62\x57\x7C\x62\x58\x7C\x62\x59\x7C\x62\x5A\x7C\x63\x30\x7C\x63\x31\x7C\x63\x32\x7C\x63\x33\x7C\x63\x34\x7C\x63\x35\x7C\x63\x36\x7C\x63\x37\x7C\x63\x38\x7C\x63\x39\x7C\x63\x61\x7C\x63\x62\x7C\x63\x63\x7C\x63\x64\x7C\x63\x65\x7C\x63\x66\x7C\x63\x67\x7C\x63\x68\x7C\x63\x69\x7C\x63\x6A\x7C\x63\x6B\x7C\x63\x6C\x7C\x63\x6D\x7C\x63\x6E\x7C\x63\x6F\x7C\x63\x70\x7C\x63\x71\x7C\x63\x72\x7C\x63\x73\x7C\x63\x74\x7C\x63\x75\x7C\x63\x76\x7C\x63\x77\x7C\x63\x78\x7C\x63\x79\x7C\x63\x7A\x7C\x63\x41\x7C\x63\x42\x7C\x63\x43\x7C\x63\x44\x7C\x63\x45\x7C\x63\x46\x7C\x63\x47\x7C\x63\x48\x7C\x63\x49\x7C\x63\x4A\x7C\x63\x4B\x7C\x63\x4C\x7C\x63\x4D\x7C\x63\x4E\x7C\x63\x4F\x7C\x63\x50\x7C\x63\x51\x7C\x63\x52\x7C\x63\x53\x7C\x63\x54\x7C\x63\x55\x7C\x63\x56\x7C\x63\x57\x7C\x63\x58\x7C\x63\x59\x7C\x63\x5A\x7C\x64\x30\x7C\x64\x31\x7C\x64\x32\x7C\x64\x33\x7C\x64\x34\x7C\x64\x35\x7C\x64\x36\x7C\x64\x37\x7C\x64\x38\x7C\x64\x39\x7C\x64\x61\x7C\x64\x62\x7C\x64\x63\x7C\x64\x64\x7C\x64\x65\x7C\x64\x66\x7C\x64\x67\x7C\x64\x68\x7C\x64\x69\x7C\x64\x6A\x7C\x64\x6B\x7C\x64\x6C\x7C\x64\x6D\x7C\x64\x6E\x7C\x64\x6F\x7C\x64\x70\x7C\x64\x71\x7C\x64\x72\x7C\x64\x73\x7C\x64\x74\x7C\x64\x75\x7C\x64\x76\x7C\x64\x77\x7C\x64\x78\x7C\x64\x79\x7C\x64\x7A\x7C\x64\x41\x7C\x64\x42\x7C\x64\x43\x7C\x64\x44\x7C\x64\x45\x7C\x64\x46\x7C\x64\x47\x7C\x64\x48\x7C\x64\x49\x7C\x64\x4A\x7C\x64\x4B\x7C\x64\x4C\x7C\x64\x4D\x7C\x64\x4E\x7C\x64\x4F\x7C\x64\x50\x7C\x64\x51\x7C\x64\x52\x7C\x64\x53\x7C\x64\x54\x7C\x64\x55\x7C\x64\x56\x7C\x64\x57\x7C\x64\x58\x7C\x64\x59\x7C\x64\x5A\x7C\x65\x30\x7C\x65\x31\x7C\x65\x32\x7C\x65\x33\x7C\x65\x34\x7C\x65\x35\x7C\x65\x36\x7C\x65\x37\x7C\x65\x38\x7C\x65\x39\x7C\x65\x61\x7C\x65\x62\x7C\x65\x63\x7C\x65\x64\x7C\x65\x65\x7C\x65\x66\x7C\x65\x67\x7C\x65\x68\x7C\x65\x69\x7C\x65\x6A\x7C\x65\x6B\x7C\x65\x6C\x7C\x65\x6D\x7C\x65\x6E\x7C\x65\x6F\x7C\x65\x70\x7C\x65\x71\x7C\x65\x72\x7C\x65\x73\x7C\x65\x74\x7C\x65\x75\x7C\x65\x76\x7C\x65\x77\x7C\x65\x78\x7C\x65\x79\x7C\x65\x7A\x7C\x65\x41\x7C\x65\x42\x7C\x37\x41\x7C\x65\x43\x7C\x65\x44\x7C\x65\x45\x7C\x65\x46\x7C\x65\x47\x7C\x65\x48\x7C\x65\x49\x7C\x65\x4A\x7C\x65\x4B\x7C\x65\x4C\x7C\x65\x4D\x7C\x65\x4E\x27\x2E\x65\x4F\x28\x27\x7C\x27\x29\x2C\x30\x2C\x7B\x7D\x29\x29","\x7C","\x73\x70\x6C\x69\x74","\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x66\x75\x6E\x63\x74\x69\x6F\x6E\x7C\x72\x65\x74\x75\x72\x6E\x7C\x53\x74\x72\x69\x6E\x67\x7C\x69\x66\x7C\x77\x68\x69\x6C\x65\x7C\x70\x61\x72\x73\x65\x49\x6E\x74\x7C\x72\x65\x70\x6C\x61\x63\x65\x7C\x6E\x65\x77\x7C\x65\x76\x61\x6C\x7C\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65\x7C\x74\x6F\x53\x74\x72\x69\x6E\x67\x7C\x52\x65\x67\x45\x78\x70\x7C\x34\x36\x38\x7C\x78\x33\x30\x7C\x78\x37\x38\x7C\x78\x33\x31\x7C\x78\x33\x32\x7C\x78\x36\x35\x7C\x78\x36\x31\x7C\x78\x37\x34\x7C\x78\x37\x33\x7C\x78\x36\x66\x7C\x78\x36\x33\x7C\x78\x36\x34\x7C\x78\x36\x63\x7C\x78\x36\x32\x7C\x78\x37\x32\x7C\x78\x36\x39\x7C\x78\x36\x36\x7C\x78\x36\x65\x7C\x78\x32\x64\x7C\x78\x37\x30\x7C\x78\x36\x64\x7C\x78\x33\x34\x7C\x78\x33\x35\x7C\x78\x33\x36\x7C\x78\x33\x37\x7C\x78\x33\x33\x7C\x78\x36\x38\x7C\x78\x37\x35\x7C\x76\x61\x72\x7C\x78\x33\x39\x7C\x78\x32\x30\x7C\x78\x33\x38\x7C\x78\x36\x37\x7C\x78\x32\x65\x7C\x78\x32\x66\x7C\x78\x32\x32\x7C\x78\x33\x65\x7C\x78\x37\x39\x7C\x78\x37\x37\x7C\x78\x33\x63\x7C\x78\x33\x64\x7C\x78\x37\x36\x7C\x74\x68\x69\x73\x7C\x65\x6C\x73\x65\x7C\x30\x78\x30\x7C\x78\x36\x62\x7C\x78\x34\x31\x7C\x78\x35\x34\x7C\x78\x34\x33\x7C\x78\x33\x61\x7C\x30\x78\x31\x7C\x78\x34\x63\x7C\x78\x35\x37\x7C\x78\x32\x33\x7C\x78\x37\x64\x7C\x78\x35\x33\x7C\x78\x37\x62\x7C\x78\x32\x63\x7C\x78\x34\x39\x7C\x5F\x30\x78\x31\x62\x63\x34\x38\x38\x7C\x78\x37\x31\x7C\x78\x34\x36\x7C\x5F\x30\x78\x35\x38\x32\x37\x36\x37\x7C\x78\x35\x66\x7C\x78\x34\x35\x7C\x78\x37\x61\x7C\x78\x35\x30\x7C\x78\x36\x61\x7C\x78\x34\x66\x7C\x78\x34\x65\x7C\x78\x35\x35\x7C\x78\x32\x34\x7C\x78\x34\x32\x7C\x78\x34\x38\x7C\x78\x35\x39\x7C\x78\x34\x34\x7C\x78\x35\x36\x7C\x78\x34\x37\x7C\x78\x35\x31\x7C\x78\x33\x62\x7C\x5F\x30\x78\x31\x62\x32\x38\x7C\x78\x34\x61\x7C\x78\x34\x62\x7C\x78\x35\x32\x7C\x78\x32\x31\x7C\x5F\x30\x78\x33\x38\x62\x39\x36\x38\x7C\x5F\x30\x78\x31\x36\x36\x66\x65\x33\x7C\x78\x34\x64\x7C\x5F\x30\x78\x64\x39\x37\x64\x61\x35\x7C\x5F\x30\x78\x35\x65\x33\x33\x32\x64\x7C\x30\x78\x31\x66\x34\x7C\x78\x32\x62\x7C\x5F\x30\x78\x32\x66\x36\x61\x62\x66\x7C\x30\x78\x61\x61\x7C\x63\x6F\x6E\x73\x74\x7C\x78\x35\x38\x7C\x5F\x30\x78\x64\x33\x63\x65\x39\x30\x7C\x30\x78\x61\x7C\x66\x6F\x72\x7C\x30\x78\x66\x61\x7C\x5F\x30\x78\x33\x39\x30\x66\x38\x32\x7C\x5F\x30\x78\x33\x64\x31\x64\x34\x38\x7C\x5F\x30\x78\x33\x62\x31\x33\x62\x31\x7C\x5F\x30\x78\x64\x66\x65\x38\x30\x66\x7C\x5F\x30\x78\x63\x61\x38\x31\x37\x64\x7C\x5F\x30\x78\x33\x62\x38\x32\x36\x35\x7C\x30\x78\x33\x7C\x5F\x30\x78\x35\x63\x33\x32\x7C\x6E\x75\x6C\x6C\x7C\x77\x69\x6E\x64\x6F\x77\x7C\x74\x79\x70\x65\x6F\x66\x7C\x5F\x30\x78\x34\x66\x64\x36\x32\x39\x7C\x78\x35\x61\x7C\x5F\x30\x78\x35\x35\x62\x34\x62\x39\x7C\x5F\x30\x78\x32\x30\x35\x38\x38\x64\x7C\x5F\x30\x78\x39\x35\x31\x31\x39\x38\x7C\x5F\x30\x78\x35\x35\x36\x66\x35\x64\x7C\x5F\x30\x78\x37\x39\x62\x37\x31\x37\x7C\x5F\x30\x78\x65\x61\x34\x34\x36\x66\x7C\x5F\x30\x78\x32\x38\x32\x34\x62\x63\x7C\x4D\x61\x74\x68\x7C\x6E\x6F\x54\x68\x75\x6D\x62\x6E\x61\x69\x6C\x7C\x30\x78\x31\x65\x7C\x5F\x30\x78\x34\x36\x37\x65\x38\x64\x7C\x5F\x30\x78\x34\x33\x38\x38\x33\x38\x7C\x5F\x30\x78\x35\x38\x65\x62\x36\x36\x7C\x5F\x30\x78\x35\x39\x62\x31\x33\x61\x7C\x64\x61\x72\x6B\x4D\x6F\x64\x65\x7C\x75\x73\x65\x72\x44\x61\x72\x6B\x4D\x6F\x64\x65\x7C\x6C\x6F\x63\x61\x6C\x53\x74\x6F\x72\x61\x67\x65\x7C\x5F\x30\x78\x65\x33\x33\x61\x34\x61\x7C\x5F\x30\x78\x31\x36\x62\x38\x65\x34\x7C\x5F\x30\x78\x35\x65\x37\x63\x63\x39\x7C\x5F\x30\x78\x34\x32\x63\x36\x37\x65\x7C\x78\x32\x36\x7C\x5F\x30\x78\x33\x37\x39\x30\x31\x64\x7C\x5F\x30\x78\x34\x34\x64\x37\x66\x37\x7C\x5F\x30\x78\x35\x32\x34\x65\x32\x35\x7C\x5F\x30\x78\x33\x30\x34\x64\x35\x30\x7C\x61\x72\x67\x75\x6D\x65\x6E\x74\x73\x7C\x5F\x30\x78\x33\x62\x34\x34\x36\x62\x7C\x5F\x30\x78\x62\x62\x62\x34\x35\x34\x7C\x5F\x30\x78\x33\x36\x63\x34\x62\x38\x7C\x5F\x30\x78\x34\x34\x33\x34\x32\x36\x7C\x5F\x30\x78\x33\x65\x38\x64\x66\x36\x7C\x78\x32\x35\x7C\x5F\x30\x78\x31\x32\x39\x31\x32\x64\x7C\x5F\x30\x78\x31\x63\x64\x37\x63\x32\x7C\x5F\x30\x78\x35\x61\x35\x35\x38\x36\x7C\x5F\x30\x78\x31\x32\x30\x61\x30\x64\x7C\x5F\x30\x78\x35\x30\x31\x61\x66\x33\x7C\x5F\x30\x78\x34\x61\x39\x63\x39\x33\x7C\x5F\x30\x78\x32\x37\x64\x64\x39\x31\x7C\x5F\x30\x78\x35\x64\x39\x32\x38\x36\x7C\x5F\x30\x78\x35\x61\x36\x62\x36\x36\x7C\x64\x6F\x63\x75\x6D\x65\x6E\x74\x7C\x5F\x30\x78\x31\x34\x30\x38\x64\x61\x7C\x5F\x30\x78\x33\x39\x63\x30\x65\x64\x7C\x5F\x30\x78\x35\x31\x31\x62\x38\x66\x7C\x5F\x30\x78\x33\x65\x35\x36\x30\x62\x7C\x5F\x30\x78\x34\x31\x33\x66\x36\x36\x7C\x5F\x30\x78\x33\x31\x38\x65\x37\x37\x7C\x5F\x30\x78\x35\x61\x32\x64\x63\x38\x7C\x5F\x30\x78\x34\x61\x34\x61\x34\x39\x7C\x5F\x30\x78\x35\x66\x31\x61\x35\x32\x7C\x78\x33\x66\x7C\x78\x32\x38\x7C\x78\x32\x39\x7C\x30\x78\x32\x7C\x30\x78\x34\x7C\x30\x78\x35\x7C\x30\x78\x37\x7C\x30\x78\x38\x7C\x62\x72\x65\x61\x6B\x7C\x70\x75\x73\x68\x7C\x73\x68\x69\x66\x74\x7C\x5F\x30\x78\x31\x63\x34\x35\x61\x34\x7C\x30\x78\x31\x34\x7C\x5F\x30\x78\x65\x61\x36\x61\x63\x65\x7C\x5F\x30\x78\x34\x33\x30\x33\x61\x64\x7C\x5F\x30\x78\x34\x61\x33\x62\x63\x37\x7C\x5F\x30\x78\x38\x61\x62\x62\x62\x64\x7C\x30\x78\x33\x65\x38\x7C\x5F\x30\x78\x35\x39\x31\x61\x38\x62\x7C\x5F\x30\x78\x33\x66\x32\x66\x35\x37\x7C\x5F\x30\x78\x35\x31\x35\x30\x30\x33\x7C\x5F\x30\x78\x34\x36\x61\x38\x63\x62\x7C\x5F\x30\x78\x35\x62\x37\x33\x37\x31\x7C\x5F\x30\x78\x34\x65\x36\x63\x33\x35\x7C\x5F\x30\x78\x32\x62\x37\x39\x63\x37\x7C\x5F\x30\x78\x34\x37\x35\x33\x30\x63\x7C\x5F\x30\x78\x33\x31\x31\x33\x31\x63\x7C\x5F\x30\x78\x31\x37\x63\x34\x64\x34\x7C\x5F\x30\x78\x32\x62\x66\x35\x37\x65\x7C\x5F\x30\x78\x37\x65\x34\x64\x63\x35\x7C\x5F\x30\x78\x34\x33\x38\x64\x63\x62\x7C\x30\x78\x34\x36\x7C\x5F\x30\x78\x33\x36\x62\x34\x62\x36\x7C\x5F\x30\x78\x35\x64\x38\x30\x33\x32\x7C\x5F\x30\x78\x34\x32\x38\x65\x33\x35\x7C\x5F\x30\x78\x35\x65\x63\x34\x32\x63\x7C\x5F\x30\x78\x31\x31\x38\x62\x34\x37\x7C\x5F\x30\x78\x31\x35\x36\x35\x37\x64\x7C\x5F\x30\x78\x31\x63\x37\x62\x61\x35\x7C\x5F\x30\x78\x37\x34\x30\x63\x66\x30\x7C\x5F\x30\x78\x32\x38\x31\x66\x38\x38\x7C\x5F\x30\x78\x33\x39\x31\x66\x30\x37\x7C\x5F\x30\x78\x34\x35\x39\x34\x7C\x5F\x30\x78\x31\x33\x62\x35\x37\x32\x7C\x5F\x30\x78\x31\x34\x63\x65\x31\x35\x7C\x5F\x30\x78\x31\x61\x30\x65\x30\x37\x7C\x5F\x30\x78\x32\x34\x33\x34\x33\x36\x7C\x5F\x30\x78\x35\x34\x63\x38\x31\x39\x7C\x5F\x30\x78\x35\x31\x34\x36\x65\x36\x7C\x5F\x30\x78\x33\x30\x36\x31\x30\x38\x7C\x5F\x30\x78\x33\x38\x61\x63\x35\x36\x7C\x5F\x30\x78\x33\x37\x36\x63\x34\x30\x7C\x5F\x30\x78\x32\x32\x66\x37\x33\x34\x7C\x5F\x30\x78\x35\x61\x64\x31\x34\x30\x7C\x69\x66\x72\x61\x6D\x65\x7C\x73\x72\x63\x7C\x77\x77\x77\x7C\x79\x6F\x75\x74\x75\x62\x65\x7C\x63\x6F\x6D\x7C\x5F\x30\x78\x37\x30\x30\x63\x35\x66\x7C\x5F\x30\x78\x31\x35\x37\x32\x37\x32\x7C\x75\x6E\x64\x65\x66\x69\x6E\x65\x64\x7C\x5F\x30\x78\x31\x62\x33\x32\x30\x36\x7C\x5F\x30\x78\x33\x34\x33\x63\x36\x35\x7C\x5F\x30\x78\x32\x36\x64\x32\x31\x33\x7C\x5F\x30\x78\x31\x35\x61\x32\x61\x36\x7C\x5F\x30\x78\x35\x39\x61\x37\x65\x38\x7C\x5F\x30\x78\x32\x33\x63\x34\x34\x37\x7C\x5F\x30\x78\x32\x62\x35\x64\x62\x32\x7C\x5F\x30\x78\x31\x38\x31\x34\x64\x63\x7C\x5F\x30\x78\x31\x35\x63\x30\x34\x62\x7C\x5F\x30\x78\x35\x38\x35\x39\x39\x37\x7C\x5F\x30\x78\x32\x61\x61\x38\x30\x36\x7C\x5F\x30\x78\x32\x33\x37\x39\x61\x65\x7C\x5F\x30\x78\x35\x66\x66\x39\x32\x38\x7C\x5F\x30\x78\x62\x34\x32\x34\x64\x30\x7C\x5F\x30\x78\x35\x33\x39\x66\x34\x61\x7C\x5F\x30\x78\x35\x63\x33\x39\x62\x61\x7C\x74\x72\x79\x7C\x30\x78\x36\x7C\x30\x78\x39\x7C\x30\x78\x62\x7C\x63\x61\x74\x63\x68\x7C\x5F\x30\x78\x34\x36\x65\x36\x33\x30\x7C\x30\x78\x61\x63\x39\x65\x34\x7C\x5F\x30\x78\x32\x63\x34\x37\x38\x64\x7C\x5F\x30\x78\x35\x36\x66\x33\x37\x65\x7C\x5F\x30\x78\x31\x32\x35\x66\x65\x65\x7C\x5F\x30\x78\x35\x65\x34\x39\x32\x32\x7C\x5F\x30\x78\x32\x63\x35\x35\x36\x63\x7C\x5F\x30\x78\x63\x65\x38\x66\x33\x66\x7C\x5F\x30\x78\x33\x36\x65\x38\x65\x63\x7C\x5F\x30\x78\x33\x62\x37\x34\x30\x62\x7C\x5F\x30\x78\x31\x36\x61\x61\x62\x33\x7C\x5F\x30\x78\x36\x62\x36\x32\x36\x39\x7C\x5F\x30\x78\x31\x65\x34\x32\x32\x31\x7C\x5F\x30\x78\x61\x34\x37\x61\x35\x35\x7C\x5F\x30\x78\x31\x38\x62\x38\x30\x34\x7C\x49\x6D\x61\x67\x65\x7C\x5F\x30\x78\x31\x36\x36\x64\x32\x66\x7C\x5F\x30\x78\x31\x35\x36\x35\x65\x63\x7C\x5F\x30\x78\x64\x33\x63\x61\x64\x34\x7C\x5F\x30\x78\x33\x32\x66\x38\x39\x35\x7C\x5F\x30\x78\x31\x31\x36\x35\x35\x62\x7C\x5F\x30\x78\x34\x35\x61\x37\x63\x36\x7C\x5F\x30\x78\x35\x36\x30\x32\x38\x39\x7C\x5F\x30\x78\x32\x32\x35\x34\x62\x30\x7C\x5F\x30\x78\x34\x37\x32\x65\x31\x36\x7C\x5F\x30\x78\x34\x62\x35\x65\x36\x63\x7C\x5F\x30\x78\x34\x63\x38\x61\x34\x31\x7C\x5F\x30\x78\x33\x34\x38\x30\x30\x36\x7C\x6A\x51\x75\x65\x72\x79\x7C\x73\x65\x74\x49\x6E\x74\x65\x72\x76\x61\x6C\x7C\x5F\x30\x78\x33\x65\x32\x62\x34\x33\x7C\x5F\x30\x78\x31\x61\x39\x65\x61\x39\x7C\x5F\x30\x78\x31\x38\x62\x63\x61\x63\x7C\x5F\x30\x78\x38\x65\x30\x65\x62\x36\x7C\x5F\x30\x78\x31\x31\x32\x36\x37\x36\x7C\x5F\x30\x78\x32\x34\x66\x33\x36\x38\x7C\x5F\x30\x78\x31\x61\x66\x33\x61\x62\x7C\x5F\x30\x78\x33\x37\x38\x37\x36\x35\x7C\x5F\x30\x78\x31\x66\x39\x64\x39\x64\x7C\x5F\x30\x78\x33\x63\x33\x63\x65\x33\x7C\x5F\x30\x78\x34\x37\x63\x63\x30\x63\x7C\x5F\x30\x78\x35\x64\x39\x31\x31\x66\x7C\x5F\x30\x78\x32\x63\x38\x35\x62\x62\x7C\x5F\x30\x78\x34\x37\x30\x33\x38\x32\x7C\x5F\x30\x78\x32\x32\x30\x39\x38\x31\x7C\x5F\x30\x78\x33\x31\x63\x34\x35\x62\x7C\x5F\x30\x78\x31\x62\x37\x65\x64\x62\x7C\x5F\x30\x78\x31\x31\x30\x30\x36\x39\x7C\x5F\x30\x78\x32\x36\x36\x31\x38\x63\x7C\x5F\x30\x78\x33\x64\x65\x36\x63\x66\x7C\x5F\x30\x78\x35\x33\x37\x31\x36\x33\x7C\x5F\x30\x78\x32\x34\x36\x63\x37\x32\x7C\x5F\x30\x78\x33\x66\x35\x33\x36\x32\x7C\x5F\x30\x78\x63\x38\x30\x65\x64\x32\x7C\x5F\x30\x78\x65\x33\x61\x37\x63\x37\x7C\x5F\x30\x78\x35\x31\x63\x33\x39\x66\x7C\x5F\x30\x78\x34\x33\x32\x66\x33\x36\x7C\x5F\x30\x78\x35\x66\x34\x65\x39\x38\x7C\x5F\x30\x78\x66\x35\x38\x66\x32\x33\x7C\x70\x6F\x73\x74\x50\x65\x72\x50\x61\x67\x65\x7C\x5F\x30\x78\x31\x32\x38\x62\x61\x31\x7C\x5F\x30\x78\x34\x33\x38\x31\x36\x34\x7C\x5F\x30\x78\x32\x62\x66\x64\x62\x36\x7C\x5F\x30\x78\x34\x30\x35\x63\x63\x61\x7C\x5F\x30\x78\x31\x30\x63\x65\x64\x36\x7C\x66\x69\x78\x65\x64\x53\x69\x64\x65\x62\x61\x72\x7C\x5F\x30\x78\x31\x33\x61\x32\x32\x39\x7C\x5F\x30\x78\x35\x65\x32\x62\x32\x63\x7C\x5F\x30\x78\x32\x30\x39\x33\x30\x30\x7C\x5F\x30\x78\x32\x62\x38\x63\x32\x39\x7C\x5F\x30\x78\x33\x61\x65\x37\x64\x33\x7C\x5F\x30\x78\x33\x32\x31\x66\x62\x61\x7C\x5F\x30\x78\x35\x66\x34\x63\x63\x36\x7C\x5F\x30\x78\x34\x30\x66\x37\x61\x33\x7C\x5F\x30\x78\x32\x65\x31\x63\x33\x64\x7C\x5F\x30\x78\x31\x35\x65\x63\x64\x32\x7C\x5F\x30\x78\x35\x32\x37\x37\x39\x65\x7C\x5F\x30\x78\x32\x39\x36\x38\x35\x34\x7C\x5F\x30\x78\x35\x35\x66\x39\x62\x66\x7C\x5F\x30\x78\x31\x30\x61\x36\x30\x38\x7C\x30\x78\x36\x34\x7C\x5F\x30\x78\x62\x36\x61\x63\x66\x31\x7C\x5F\x30\x78\x35\x33\x65\x64\x66\x65\x7C\x5F\x30\x78\x35\x39\x36\x61\x38\x61\x7C\x5F\x30\x78\x34\x35\x36\x61\x62\x34\x7C\x5F\x30\x78\x35\x35\x65\x63\x37\x34\x7C\x5F\x30\x78\x34\x36\x65\x32\x36\x36\x7C\x5F\x30\x78\x34\x36\x30\x64\x37\x63\x7C\x5F\x30\x78\x32\x32\x30\x33\x63\x35\x7C\x5F\x30\x78\x35\x31\x63\x30\x38\x63\x7C\x5F\x30\x78\x32\x64\x32\x39\x38\x32\x7C\x5F\x30\x78\x31\x39\x39\x38\x61\x32\x7C\x5F\x30\x78\x33\x64\x64\x37\x34\x62\x7C\x5F\x30\x78\x66\x61\x34\x38\x34\x35\x7C\x5F\x30\x78\x35\x30\x35\x31\x64\x39\x7C\x5F\x30\x78\x33\x35\x39\x35\x34\x62\x7C\x5F\x30\x78\x33\x33\x61\x62\x33\x34\x7C\x5F\x30\x78\x34\x31\x39\x31\x37\x35\x7C\x5F\x30\x78\x33\x62\x36\x32\x30\x65\x7C\x5F\x30\x78\x33\x39\x36\x61\x64\x62\x7C\x5F\x30\x78\x33\x62\x39\x66\x62\x37\x7C\x5F\x30\x78\x34\x37\x63\x36\x30\x31\x7C\x5F\x30\x78\x35\x63\x31\x33\x31\x64\x7C\x5F\x30\x78\x34\x63\x64\x34\x32\x63\x7C\x5F\x30\x78\x32\x32\x66\x37\x63\x65\x7C\x5F\x30\x78\x61\x66\x31\x38\x62\x35\x7C\x5F\x30\x78\x32\x33\x61\x35\x34\x32\x7C\x5F\x30\x78\x35\x39\x62\x39\x35\x32\x7C\x5F\x30\x78\x35\x63\x32\x36\x39\x33\x7C\x5F\x30\x78\x34\x33\x62\x66\x61\x35\x7C\x5F\x30\x78\x35\x66\x31\x39\x36\x39\x7C\x5F\x30\x78\x35\x39\x36\x30\x38\x61\x7C\x6D\x6F\x6E\x74\x68\x46\x6F\x72\x6D\x61\x74\x7C\x5F\x30\x78\x35\x37\x37\x30\x64\x34\x7C\x5F\x30\x78\x34\x34\x37\x34\x32\x65\x7C\x5F\x30\x78\x35\x64\x66\x39\x38\x66\x7C\x5F\x30\x78\x34\x31\x63\x33\x65\x63\x7C\x5F\x30\x78\x61\x31\x36\x65\x38\x32\x7C\x5F\x30\x78\x35\x34\x38\x65\x37\x30\x7C\x5F\x30\x78\x33\x35\x30\x64\x33\x37\x7C\x5F\x30\x78\x39\x31\x32\x64\x62\x62\x7C\x5F\x30\x78\x32\x39\x30\x62\x34\x37\x7C\x5F\x30\x78\x32\x38\x35\x30\x63\x36\x7C\x5F\x30\x78\x34\x34\x39\x66\x30\x38\x7C\x5F\x30\x78\x32\x31\x32\x66\x64\x31\x7C\x5F\x30\x78\x33\x33\x65\x38\x66\x33\x7C\x5F\x30\x78\x31\x64\x32\x35\x61\x35\x7C\x5F\x30\x78\x35\x37\x31\x33\x33\x31\x7C\x5F\x30\x78\x33\x39\x38\x61\x34\x65\x7C\x5F\x30\x78\x33\x36\x39\x31\x32\x35\x7C\x5F\x30\x78\x34\x36\x34\x65\x34\x32\x7C\x5F\x30\x78\x33\x66\x33\x36\x30\x34\x7C\x5F\x30\x78\x33\x65\x34\x32\x39\x34\x7C\x5F\x30\x78\x35\x64\x37\x31\x38\x39\x7C\x5F\x30\x78\x63\x32\x63\x61\x33\x62\x7C\x5F\x30\x78\x35\x38\x65\x64\x61\x39\x7C\x5F\x30\x78\x31\x37\x35\x34\x39\x65\x7C\x5F\x30\x78\x35\x39\x34\x36\x61\x31\x7C\x5F\x30\x78\x33\x63\x37\x30\x33\x66\x7C\x5F\x30\x78\x31\x33\x62\x31\x36\x61\x7C\x5F\x30\x78\x34\x38\x65\x66\x34\x65\x7C\x5F\x30\x78\x35\x64\x38\x35\x32\x36\x7C\x5F\x30\x78\x33\x32\x35\x62\x65\x35\x7C\x5F\x30\x78\x33\x35\x62\x63\x39\x33\x7C\x5F\x30\x78\x32\x33\x39\x39\x64\x32\x7C\x5F\x30\x78\x33\x66\x34\x30\x66\x34\x7C\x5F\x30\x78\x35\x38\x64\x31\x37\x34\x7C\x5F\x30\x78\x35\x33\x39\x32\x35\x31\x7C\x5F\x30\x78\x33\x35\x63\x34\x61\x34\x7C\x5F\x30\x78\x33\x34\x66\x39\x36\x65\x7C\x5F\x30\x78\x62\x32\x64\x62\x65\x61\x7C\x5F\x30\x78\x35\x36\x39\x61\x61\x64\x7C\x5F\x30\x78\x31\x61\x63\x64\x35\x38\x7C\x5F\x30\x78\x34\x34\x35\x33\x33\x38\x7C\x5F\x30\x78\x32\x62\x39\x61\x33\x66\x7C\x5F\x30\x78\x32\x39\x39\x63\x65\x31\x7C\x5F\x30\x78\x33\x31\x63\x61\x61\x61\x7C\x63\x6F\x6D\x6D\x65\x6E\x74\x73\x53\x79\x73\x74\x65\x6D\x7C\x5F\x30\x78\x33\x36\x64\x32\x31\x64\x7C\x64\x69\x73\x71\x75\x73\x5F\x62\x6C\x6F\x67\x67\x65\x72\x5F\x63\x75\x72\x72\x65\x6E\x74\x5F\x75\x72\x6C\x7C\x6C\x6F\x63\x61\x74\x69\x6F\x6E\x7C\x5F\x30\x78\x32\x61\x36\x63\x66\x32\x7C\x5F\x30\x78\x35\x37\x66\x64\x63\x37\x7C\x5F\x30\x78\x35\x61\x34\x31\x64\x31\x7C\x5F\x30\x78\x32\x36\x62\x66\x66\x38\x7C\x5F\x30\x78\x31\x39\x61\x64\x62\x35\x7C\x5F\x30\x78\x34\x63\x30\x30\x35\x36\x7C\x5F\x30\x78\x32\x64\x34\x32\x37\x38\x7C\x64\x69\x73\x71\x75\x73\x53\x68\x6F\x72\x74\x6E\x61\x6D\x65\x7C\x5F\x30\x78\x32\x63\x65\x32\x63\x65\x7C\x5F\x30\x78\x31\x35\x37\x61\x65\x39\x7C\x5F\x30\x78\x35\x62\x37\x66\x31\x63\x7C\x5F\x30\x78\x37\x33\x64\x32\x66\x38\x7C\x5F\x30\x78\x35\x61\x36\x34\x63\x38\x7C\x5F\x30\x78\x34\x63\x33\x35\x33\x64\x7C\x5F\x30\x78\x31\x38\x35\x32\x61\x66\x7C\x5F\x30\x78\x34\x33\x62\x31\x62\x66\x7C\x5F\x30\x78\x32\x35\x61\x66\x37\x34\x7C\x30\x78\x63\x32\x7C\x5F\x30\x78\x33\x30\x34\x62\x66\x38\x7C\x5F\x30\x78\x33\x61\x37\x64\x33\x38\x7C\x5F\x30\x78\x34\x39\x65\x37\x33\x30\x7C\x5F\x30\x78\x34\x65\x36\x31\x62\x36\x7C\x5F\x30\x78\x33\x63\x37\x62\x32\x66\x7C\x5F\x30\x78\x33\x63\x30\x36\x37\x64\x7C\x5F\x30\x78\x65\x30\x66\x65\x64\x7C\x5F\x30\x78\x34\x38\x30\x39\x36\x36\x7C\x5F\x30\x78\x31\x36\x36\x36\x30\x62\x7C\x5F\x30\x78\x33\x34\x35\x38\x33\x65\x7C\x5F\x30\x78\x34\x30\x62\x61\x34\x64\x7C\x73\x70\x6C\x69\x74","","\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65","\x72\x65\x70\x6C\x61\x63\x65","\x5C\x77\x2B","\x5C\x62","\x67"];eval(function(_0x45fdx1,_0x45fdx2,_0x45fdx3,_0x45fdx4,_0x45fdx5,_0x45fdx6){_0x45fdx5= function(_0x45fdx3){return (_0x45fdx3< _0x45fdx2?_0x9125[4]:_0x45fdx5(parseInt(_0x45fdx3/ _0x45fdx2)))+ ((_0x45fdx3= _0x45fdx3% _0x45fdx2)> 35?String[_0x9125[5]](_0x45fdx3+ 29):_0x45fdx3.toString(36))};if(!_0x9125[4][_0x9125[6]](/^/,String)){while(_0x45fdx3--){_0x45fdx6[_0x45fdx5(_0x45fdx3)]= _0x45fdx4[_0x45fdx3]|| _0x45fdx5(_0x45fdx3)};_0x45fdx4= [function(_0x45fdx5){return _0x45fdx6[_0x45fdx5]}];_0x45fdx5= function(){return _0x9125[7]};_0x45fdx3= 1};while(_0x45fdx3--){if(_0x45fdx4[_0x45fdx3]){_0x45fdx1= _0x45fdx1[_0x9125[6]]( new RegExp(_0x9125[8]+ _0x45fdx5(_0x45fdx3)+ _0x9125[8],_0x9125[9]),_0x45fdx4[_0x45fdx3])}};return _0x45fdx1}(_0x9125[0],62,919,_0x9125[3][_0x9125[2]](_0x9125[1]),0,{}))
//]]>
</script>

<!-- Pagination Scripts -->
<b:if cond='data:view.isMultipleItems'>
<script type='text/javascript'>
//<![CDATA[
$(function() {
 $("#load-more-link")["each"](function() {
        var a = $(this),
            b = a["data"]("load");
        if (b) $("#load-more-link")["show"]();
        $("#load-more-link")["on"]("click", function(a) {
            $("#load-more-link")["hide"]();
            $["ajax"]({
                url: b,
                success: function(a) {
                    var c = $(a)["find"](".grid-posts");
                    c["find"](".index-post")["addClass"]("post-animated post-fadeInUp");
                    $(".grid-posts")["append"](c["html"]());
                    b = $(a)["find"]("#load-more-link")["data"]("load");
                    if (b) $("#load-more-link")["show"]();
                    else {
                        $("#load-more-link")["hide"]();
                        $("#blog-pager .no-more")["addClass"]("show");
                    }
$('.index-post .post-image-link .post-thumb').lazyyard();
$("#main-wrapper").each(function() {
                        if (true == fixedSidebar) $(this).theiaStickySidebar();
                    });
                },
                beforeSend: function() {
                    $("#blog-pager .loading")["show"]();
                },
                complete: function() {
                    $("#blog-pager .loading")["hide"]();
                }
            });
            a["preventDefault"]();
        });

    });
});
//]]>
</script>
</b:if>

<!-- Facebook SDK -->
<script type='text/javascript'>
//<![CDATA[
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = 'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
//]]>
</script>  
<!-- Overlay and Back To Top --> 
  <div class='back-top' title='Back to Top'/>
</body>
</html>