const test = require('node:test');
const assert = require('node:assert/strict');
const { sum } = require('./index');
test('smoke: module can build and execute', () => assert.equal(sum(2, 3), 5));
