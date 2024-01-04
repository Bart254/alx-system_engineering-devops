#installs package flask fron pip3
package { 'flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider => pip3,
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => pip3
}
