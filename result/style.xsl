<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <!-- Root template -->
  <xsl:template match="/">
    <html>
    <link rel="stylesheet" type="text/css" href="style.css"/>

      <body>
        <h1>La tête de Martin: Comédie en un acte</h1>
        <xsl:apply-templates select="body/*"/>
      </body>
    </html>
  </xsl:template>

  <!-- Scene title -->
  <xsl:template match="head">
    <h2><xsl:value-of select="."/></h2>
  </xsl:template>

  <!-- Speaker block -->
  <xsl:template match="sp">
    <div class="speech">
      <h3>
        <xsl:value-of select="speaker"/>
        <xsl:if test="cue">
          <xsl:text> </xsl:text>
          <xsl:value-of select="cue"/>
        </xsl:if>
        <xsl:if test="p/stage">
          <i>
          <xsl:text> </xsl:text>
          <xsl:value-of select="p/stage"/>
           </i>
        </xsl:if>
       
      </h3>
      <p>
        <xsl:apply-templates select="p/node()[not(self::stage)]"/>
      </p>
    </div>
  </xsl:template>

  <!-- Paragraph: pass to inner nodes (except stage already handled) -->
  <xsl:template match="p">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- Stage direction -->
  <xsl:template match="stage">
    <i><xsl:value-of select="."/></i>
  </xsl:template>

  <!-- Cue -->
  <xsl:template match="cue">
    <b><xsl:value-of select="."/></b>
  </xsl:template>

  <!-- Inline line (poetry, etc.) -->
  <xsl:template match="l">
    <br/><xsl:value-of select="."/>
  </xsl:template>

</xsl:stylesheet>
