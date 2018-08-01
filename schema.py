from graphene import ObjectType, Field, List, String, Boolean, Int, Float


class Token(ObjectType):
    """An individual token — a word, punctuation symbol, whitespace, etc."""

    text = String(description="Verbatim text")
    text_with_ws = String(description="Text with trailing space, if present")
    orth = Int(description="ID of the verbatim text content")
    i = Int(description="Index of the token within the parent Doc")
    idx = Int(description="Character offset of the token within parent Doc")
    head_i = Int(description="Index of the token's head")
    lower = Int(description="Lowercase form")
    lower_ = String(description="Lowercase form")
    shape = Int(description="Transform of token text, to show orthographic features")
    shape_ = String(description="Transform of token text, to show orthographic features")
    lemma = Int(description="Base form of the token")
    lemma_ = String(description="Base form of the token")
    norm = Int(description="Normalized form of the token")
    norm_ = String(description="Normalized form of the token")
    pos = Int(description="Coarse-grained part-of-speech tag")
    pos_ = String(description="Coarse-grained part-of-speech tag")
    tag = Int(description="Fine-grained part-of-speech tag")
    tag_ = String(description="Fine-grained part-of-speech tag")
    dep = Int(description="Dependency label")
    dep_ = String(description="Dependency label")
    ent_type = Int(description="Named entity type")
    ent_type_ = String(description="Named entity type")
    ent_iob = Int(description="IOB code of named entity tag")
    ent_iob_ = String(description="IOB code of named entity tag")
    is_alpha = Boolean(description="Does the token consist of alphabetic characters?")
    is_ascii = Boolean(description="Does the token consist of ASCII characters?")
    is_digit = Boolean(description="Does the token consist of digits?")
    is_lower = Boolean(description="Is the token lowercase?")
    is_upper = Boolean(description="Is the token uppercase?")
    is_title = Boolean(description="Is the token titlecase?")
    is_punct = Boolean(description="Is the token punctuation?")
    is_left_punct = Boolean(description="Is the token left punctuation?")
    is_right_punct = Boolean(description="Is the token right punctuation?")
    is_space = Boolean(description="Does the token consist of whitespace characters?")
    is_bracket = Boolean(description="Is the token a bracket?")
    is_quote = Boolean(description="Is the token a quotation mark?")
    is_stop = Boolean(description="Is the token a stop word?")
    like_num = Boolean(description="Does the token resemble a number?")
    like_url = Boolean(description="Does the token resemble a URL?")
    like_email = Boolean(description="Does the token resemble an email address?")


class Span(ObjectType):
    """A slice from a Doc object"""

    text = String(description="Verbatim text")
    text_with_ws = String(description="Text with trailing space, if present")
    start = Int(description="The token offset for the start of the span")
    end = Int(description="The token offset for the end of the span")
    start_char = Int(description="The character offset for the start of the span")
    end_char = Int(description="The character offset for the end of the span.")
    label = Int(description="The span's label")
    label_ = String(description="The span's label")


class Cat(ObjectType):
    """A text category predicted by the text classifier"""

    label = String(description="The name of the category")
    score = Float(description="The score predicted for the category")


class Doc(ObjectType):
    """A sequence of Token objects and a container for accessing linguistic
    annotations."""

    text = String(description="Verbatim text")
    text_with_ws = String(description="Text with trailing space, if present")
    tokens = List(Token, description="The tokens in the document")
    ents = List(Span, description="The named entities in the document")
    sents = List(Span, description="The sentences in the document")
    cats = List(Cat, description="The text classification categories, if available")


class Meta(ObjectType):
    """The current model's meta information."""

    lang = String(description="Model language")
    name = String(description="Model name")
    license = String(description="Model license")
    author = String(description="Model author")
    url = String(description="Model author URL")
    email = String(description="Model author email")
    description = String(description="Model description")
    pipeline = List(String, description="Names of model pipeline components")
    sources = List(String, description="Training data sources")


class NLP(ObjectType):
    """Container for processing results and meta information."""

    doc = Field(Doc, description="The processed document")
    meta = Field(Meta, description="The current model's meta information")
