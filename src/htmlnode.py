
from __future__ import annotations
from enum import Enum
from typing import Optional

class HTMLNode:

    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list[HTMLNode] | None = None,
            props: dict[str, str] | None = None,
            ):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def __eq__(self, other):
        if not isinstance(other,HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props)
    
    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        if sefl.props is None:
            return ""
        rstr=""
        for key in self.props:
            rstr=rstr + f" {key}=\"{self.props[key]}\""
        return rstr

    def __repr__(self):
        return (f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})")
